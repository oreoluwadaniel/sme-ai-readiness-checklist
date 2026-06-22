from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas as Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import os

# ── Paths
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT_DIR, exist_ok=True)

# ── Fonts ─────────────────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont("WS",   f"{FD}/WorkSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("WSB",  f"{FD}/WorkSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("WSI",  f"{FD}/WorkSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("IPS",  f"{FD}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("IPSB", f"{FD}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("IPSI", f"{FD}/IBMPlexSerif-Italic.ttf"))

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0D1F3C")
NAVY_MID   = colors.HexColor("#0E2448")
TEAL       = colors.HexColor("#0A8A9A")
TEAL_PALE  = colors.HexColor("#E6F4F6")
GOLD       = colors.HexColor("#C8963E")
GOLD_PALE  = colors.HexColor("#FFF5E6")
INK        = colors.HexColor("#111827")
GREY_MED   = colors.HexColor("#6B7280")
GREY_PALE  = colors.HexColor("#F3F4F6")
BODY_BG    = colors.HexColor("#F8F7F4")
WHITE      = colors.white
SCORE_BLUE = colors.HexColor("#EEF2FF")

W, H = A4
OUT = os.path.join(OUT_DIR, "AI_Readiness_Checklist_Daniel_Olatunji.pdf")

def P(text, font="WS", size=9, color=INK, leading=None, align=TA_LEFT):
    if leading is None:
        leading = size * 1.45
    return Paragraph(text, ParagraphStyle("_", fontName=font, fontSize=size,
                     leading=leading, textColor=color, alignment=align))


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1: COVER
# ─────────────────────────────────────────────────────────────────────────────
def cover(c, w, h):

    # Full background
    c.setFillColor(NAVY)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Diagonal accent polygon
    c.setFillColor(NAVY_MID)
    path = c.beginPath()
    path.moveTo(0, h * 0.62)
    path.lineTo(w * 0.55, h)
    path.lineTo(w, h)
    path.lineTo(w, h * 0.74)
    path.lineTo(w * 0.28, h * 0.42)
    path.lineTo(0, h * 0.42)
    path.close()
    c.drawPath(path, fill=1, stroke=0)

    # Top bar (NO website reference)
    c.setFillColor(TEAL)
    c.rect(0, h - 50, w, 50, fill=1, stroke=0)
    c.setFont("WS", 8.5)
    c.setFillColor(WHITE)
    c.drawString(36, h - 30, "FREE RESOURCE   |   SME OPERATIONS SERIES")

    # Left accent stripe
    c.setFillColor(TEAL)
    c.rect(0, 0, 5, h - 50, fill=1, stroke=0)

    # Gold underline
    c.setStrokeColor(GOLD)
    c.setLineWidth(2)
    c.line(36, h - 82, 100, h - 82)

    # Hero text
    c.setFont("IPSB", 42)
    c.setFillColor(WHITE)
    c.drawString(36, h - 138, "SME AI Readiness")
    c.drawString(36, h - 184, "Checklist")

    c.setFont("WS", 14)
    c.setFillColor(colors.HexColor("#A8BBCC"))
    c.drawString(36, h - 216, "12 Questions to Assess Your Operations")
    c.drawString(36, h - 234, "Before Investing in AI")

    # Thin rule
    c.setStrokeColor(colors.HexColor("#1E3A5A"))
    c.setLineWidth(1)
    c.line(36, h - 252, w - 36, h - 252)

    # ── Angled preview card ───────────────────────────────────────────────────
    cx = w * 0.505
    cy = h * 0.388
    cw = 292
    ch = 372
    rad = math.radians(-8)
    cos_a, sin_a = math.cos(rad), math.sin(rad)

    c.saveState()
    c.transform(cos_a, sin_a, -sin_a, cos_a, cx - cw/2, cy - ch/2)

    # Shadow
    c.setFillColor(colors.HexColor("#04101E"))
    c.roundRect(7, -8, cw, ch, 10, fill=1, stroke=0)

    # Card body
    c.setFillColor(WHITE)
    c.roundRect(0, 0, cw, ch, 10, fill=1, stroke=0)

    # Card header
    c.setFillColor(NAVY)
    c.roundRect(0, ch - 66, cw, 66, 10, fill=1, stroke=0)
    c.rect(0, ch - 66, cw, 24, fill=1, stroke=0)

    c.setFont("WSB", 10.5)
    c.setFillColor(WHITE)
    c.drawString(14, ch - 24, "SME AI Readiness Checklist")
    c.setFont("WS", 7.5)
    c.setFillColor(colors.HexColor("#8FAABE"))
    c.drawString(14, ch - 38, "12 Questions to Assess Your Operations")
    c.drawString(14, ch - 50, "Before Investing in AI")

    # Teal left strip on card
    c.setFillColor(TEAL)
    c.roundRect(0, 0, 4, ch - 66, 2, fill=1, stroke=0)

    # Layer 1 badge
    c.setFillColor(TEAL)
    c.roundRect(14, ch - 92, 110, 16, 3, fill=1, stroke=0)
    c.setFont("WSB", 7)
    c.setFillColor(WHITE)
    c.drawString(20, ch - 82, "LAYER 1: VISIBILITY")

    # Visible questions
    groups = [
        ("Do you have a single source of truth", "for your customer data?"),
        ("Can your team describe your top 3", "operational bottlenecks in 60 secs?"),
        ("Do you track revenue by product", "line or customer segment?"),
        ("Do you know your average cost", "per manual process?"),
        ("Do your ops and finance teams work", "from the same numbers each week?"),
    ]
    yy = ch - 108
    for line1, line2 in groups:
        if yy < 18:
            break
        bx, by = 14, yy - 9.5
        c.setFillColor(TEAL_PALE)
        c.roundRect(bx, by, 10, 10, 1.5, fill=1, stroke=0)
        c.setStrokeColor(TEAL)
        c.setLineWidth(0.7)
        c.roundRect(bx, by, 10, 10, 1.5, fill=0, stroke=1)
        c.setFont("WS", 7.2)
        c.setFillColor(colors.HexColor("#374151"))
        c.drawString(30, yy - 2, line1)
        yy -= 13
        c.drawString(30, yy - 2, line2)
        yy -= 15

    # Gradient fade at bottom
    for i in range(24):
        alpha = (i / 24) ** 1.5
        c.setFillColorRGB(1, 1, 1, alpha)
        c.rect(4, i * 48/24, cw - 8, 48/24 + 1, fill=1, stroke=0)

    c.restoreState()

    # Three-layer icons
    icon_y = h * 0.16
    col_w = (w - 72) / 3
    for i, (num, title, desc) in enumerate([
        ("01", "Visibility",   "See what is really\nhappening"),
        ("02", "Automation",   "Remove manual\nrepetition"),
        ("03", "Intelligence", "Make better\ndecisions, faster"),
    ]):
        cx_i = 36 + i * col_w + col_w / 2
        c.setFillColor(TEAL)
        c.circle(cx_i, icon_y + 26, 17, fill=1, stroke=0)
        c.setFont("IPSB", 13)
        c.setFillColor(WHITE)
        c.drawCentredString(cx_i, icon_y + 21, num)
        c.setFont("WSB", 9.5)
        c.setFillColor(WHITE)
        c.drawCentredString(cx_i, icon_y + 4, title)
        c.setFont("WS", 7.8)
        c.setFillColor(colors.HexColor("#8FAABE"))
        for j, line in enumerate(desc.split("\n")):
            c.drawCentredString(cx_i, icon_y - 10 - j * 10.5, line)
        if i < 2:
            c.setStrokeColor(colors.HexColor("#1A3050"))
            c.setDash([2, 4])
            c.line(36 + (i+1)*col_w, icon_y + 22, 36 + (i+1)*col_w, icon_y + 30)
            c.setDash()

    # Footer - NAME + TITLE only, no website
    c.setFillColor(colors.HexColor("#081629"))
    c.rect(0, 0, w, 42, fill=1, stroke=0)
    c.setFont("WSB", 9)
    c.setFillColor(TEAL)
    c.drawString(36, 26, "DANIEL OLATUNJI")
    c.setFont("WS", 8.5)
    c.setFillColor(colors.HexColor("#8FAABE"))
    c.drawString(36 + c.stringWidth("DANIEL OLATUNJI", "WSB", 9) + 8, 26,
                 "|  DATA & AUTOMATION CONSULTANT")
    c.setFont("WS", 7.5)
    c.setFillColor(colors.HexColor("#4A6080"))
    c.drawString(36, 12, "Free resource. Share it. Reference it. Build on it.")

    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# QUESTION DATA
# ─────────────────────────────────────────────────────────────────────────────
LAYERS = [
    {
        "num": 1, "name": "Layer 1: Visibility",
        "tagline": "See clearly before you automate anything",
        "color": TEAL, "pale": TEAL_PALE,
        "questions": [
            ("Do you have a single source of truth for your customer data?",
             "If sales, finance, and ops each have a different spreadsheet, AI cannot fix the split. It needs one version of the truth."),
            ("Can your team describe your top three operational bottlenecks in under 60 seconds?",
             "Speed of answer reveals depth of understanding. If it takes a meeting to figure out where work slows down, the bottleneck is visibility itself."),
            ("Do you track revenue by product line, region, or customer segment?",
             "Top-line revenue without segmentation hides where growth is real and where it is carried by one lucky contract."),
            ("Do your operations team and finance team work from the same numbers each week?",
             "Two teams, one set of numbers. That is the baseline. Misaligned reporting creates delays and decisions made on bad data."),
        ],
    },
    {
        "num": 2, "name": "Layer 2: Automation",
        "tagline": "Identify what costs you time and accuracy every single day",
        "color": GOLD, "pale": GOLD_PALE,
        "questions": [
            ("Do you know your average cost per manual process (invoicing, data entry, follow-ups)?",
             "Time multiplied by wage multiplied by frequency. If you cannot calculate it, you cannot make a business case for replacing it."),
            ("Are there tasks your team performs the same way every single day without variation?",
             "Consistency is the automation signal. Fixed patterns are what tools handle best. If every case is different, judgment is required first."),
            ("Could a new team member follow a written process for your five most repeated tasks?",
             "If the process only lives in someone's head, it is not ready to automate. Documentation is not bureaucracy. It is the blueprint."),
            ("Do you currently use tools such as a CRM, ERP, or accounting software that could be better connected?",
             "Most SMEs already own the tools they need. The gap is integration. Disconnected software is value waiting to be released."),
        ],
    },
    {
        "num": 3, "name": "Layer 3: Intelligence",
        "tagline": "Prepare for decisions that previously required experience",
        "color": NAVY, "pale": SCORE_BLUE,
        "questions": [
            ("Do you have at least 12 months of clean, structured historical data in one place?",
             "Forecasting and pattern detection require history. Three months of data cannot tell you what demand looks like next quarter."),
            ("Do you know which customers are most likely to churn in the next 90 days?",
             "If you have never built a churn model, the honest answer is no. That is fine. It tells you exactly what your first AI project should be."),
            ("Can you identify which expenses are trending in the wrong direction before month-end close?",
             "Real-time cost visibility stops surprises. Businesses that only see their numbers after the month is over are always reacting."),
            ("Does your team trust data enough to make decisions from it without calling a verification meeting?",
             "Technology is rarely the bottleneck. Trust is. If people second-guess every report, the root problem is data quality and process ownership."),
            ("Do you have one named person responsible for data quality in your business?",
             "Without ownership, data degrades. It does not need to be a full-time hire. It needs to be someone whose name you can actually say."),
        ],
    },
]


def pg_header(c, w, h, right_label):
    c.setFillColor(NAVY)
    c.rect(0, h - 40, w, 40, fill=1, stroke=0)
    c.setFont("WSB", 8.5)
    c.setFillColor(TEAL)
    c.drawString(36, h - 24, "SME AI READINESS CHECKLIST")
    c.setFont("WS", 8.5)
    c.setFillColor(colors.HexColor("#8FAABE"))
    c.drawRightString(w - 36, h - 24, right_label)
    c.setFillColor(BODY_BG)
    c.rect(0, 0, w, h - 40, fill=1, stroke=0)

def pg_footer(c, w, pg, total=3, show_email=False):
    c.setFillColor(NAVY)
    c.rect(0, 0, w, 36, fill=1, stroke=0)
    c.setFont("WSB", 8)
    c.setFillColor(TEAL)
    c.drawString(36, 14, "DANIEL OLATUNJI")
    c.setFont("WS", 8)
    c.setFillColor(colors.HexColor("#8FAABE"))
    c.drawString(36 + c.stringWidth("DANIEL OLATUNJI","WSB",8) + 8, 14,
                 "|  DATA & AUTOMATION CONSULTANT")
    c.drawRightString(w - 36, 14, f"Page {pg} of {total}")

def layer_band(c, w, layer, y):
    bh = 42
    c.setFillColor(layer["pale"])
    c.rect(36, y - bh, w - 72, bh, fill=1, stroke=0)
    c.setFillColor(layer["color"])
    c.rect(36, y - bh, 4, bh, fill=1, stroke=0)
    pill_w = 72
    c.setFillColor(layer["color"])
    c.roundRect(48, y - bh + 10, pill_w, 14, 3, fill=1, stroke=0)
    c.setFont("WSB", 7)
    c.setFillColor(WHITE)
    c.drawCentredString(48 + pill_w/2, y - bh + 17, f"LAYER {layer['num']}")
    c.setFont("IPSB", 13)
    c.setFillColor(NAVY)
    c.drawString(132, y - bh + 22, layer["name"])
    c.setFont("WS", 8)
    c.setFillColor(GREY_MED)
    c.drawRightString(w - 40, y - bh + 14, layer["tagline"])
    return y - bh - 6

def question_block(c, w, qn, q, why, y, layer_color):
    bh = 52
    c.setFillColor(WHITE)
    c.roundRect(36, y - bh, w - 72, bh, 4, fill=1, stroke=0)
    c.setFillColor(layer_color)
    c.rect(36, y - bh, 4, bh, fill=1, stroke=0)
    c.setFont("WSB", 7.5)
    c.setFillColor(layer_color)
    c.drawString(48, y - 13, f"Q{qn:02d}")
    bx, by = 48, y - 31
    c.setFillColor(GREY_PALE)
    c.roundRect(bx, by, 12, 12, 2, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor("#D1D5DB"))
    c.setLineWidth(0.8)
    c.roundRect(bx, by, 12, 12, 2, fill=0, stroke=1)
    qp = P(q, "WSB", 9.5, INK, leading=13.5)
    qp.wrapOn(c, w - 72 - 78, 30)
    qp.drawOn(c, 68, y - 10 - qp.height)
    wp = P(f"<i>Why this matters:</i> {why}", "WS", 7.8, GREY_MED, leading=11.5)
    wp.wrapOn(c, w - 72 - 78, 28)
    wp.drawOn(c, 68, y - bh + 5)
    return y - bh - 5


def questions_pages(c, w, h):

    # ── PAGE 2: Layers 1 and 2 ────────────────────────────────────────────────
    pg_header(c, w, h, "Assessment Questions")
    intro = P(
        "Answer each question honestly. Score one point for YES. No partial credit. "
        "A solid NO is just as useful as a YES. It tells you exactly where to focus.",
        "WS", 9, GREY_MED, leading=13.5
    )
    intro.wrapOn(c, w - 72, 40)
    intro.drawOn(c, 36, h - 66)
    y = h - 84
    q_global = 1
    for layer in LAYERS[:2]:
        y = layer_band(c, w, layer, y)
        for q, why in layer["questions"]:
            y = question_block(c, w, q_global, q, why, y, layer["color"])
            q_global += 1
        y -= 4
    pg_footer(c, w, 2)
    c.showPage()

    # ── PAGE 3: Layer 3 + Scoring + Email CTA ────────────────────────────────
    pg_header(c, w, h, "Layer 3 + Scoring Guide")
    y = h - 52
    q_global = 9
    layer = LAYERS[2]
    y = layer_band(c, w, layer, y)
    for q, why in layer["questions"]:
        y = question_block(c, w, q_global, q, why, y, layer["color"])
        q_global += 1
    y -= 8

    # Scoring header
    c.setFillColor(GOLD)
    c.roundRect(36, y - 36, w - 72, 36, 5, fill=1, stroke=0)
    c.setFont("IPSB", 12.5)
    c.setFillColor(WHITE)
    c.drawString(52, y - 23, "Scoring Guide: What Your Total Means")
    y -= 40

    bands = [
        ("0 to 4",  "Start with Visibility",       TEAL_PALE,  TEAL,
         "You need a clear picture before anything else. Consolidate your data into one place and "
         "build a dashboard your whole team checks each week. That is your entire job right now."),
        ("5 to 8",  "Move to Automation",           GOLD_PALE,  GOLD,
         "Your visibility is solid enough. Pick your three most time-consuming manual processes, "
         "document each one properly, then find the tool that eliminates them. That sequence matters."),
        ("9 to 12", "Ready for Intelligence",       SCORE_BLUE, NAVY,
         "Your data is clean and routine processes run without you. Now apply AI to real decisions: "
         "forecasting, churn prediction, spend analysis. This is where the return becomes measurable."),
    ]
    for score_rng, label, bg, accent, desc in bands:
        bh = 56
        c.setFillColor(bg)
        c.roundRect(36, y - bh, w - 72, bh, 5, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(36, y - bh, 4, bh, fill=1, stroke=0)
        bw = 72
        c.setFillColor(accent)
        c.roundRect(48, y - 24, bw, 16, 3, fill=1, stroke=0)
        c.setFont("WSB", 8.5)
        c.setFillColor(WHITE)
        c.drawCentredString(48 + bw/2, y - 14, f"Score {score_rng}")
        c.setFont("WSB", 10)
        c.setFillColor(NAVY)
        c.drawString(130, y - 14, label)
        dp = P(desc, "WS", 8, GREY_MED, leading=11.8)
        dp.wrapOn(c, w - 72 - 104, 45)
        dp.drawOn(c, 130, y - bh + 5)
        y -= bh + 5

    # ── EMAIL CTA (only reference to contact) ─────────────────────────────────
    y -= 4
    cta_h = 50
    c.setFillColor(NAVY)
    c.roundRect(36, y - cta_h, w - 72, cta_h, 6, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(36, y - cta_h, 4, cta_h, fill=1, stroke=0)
    c.setFont("IPSB", 10.5)
    c.setFillColor(WHITE)
    c.drawString(52, y - 17, "Want to talk through your score?")
    c.setFont("WS", 8.5)
    c.setFillColor(colors.HexColor("#A8BBCC"))
    c.drawString(52, y - 31, "Send your score and your top bottleneck and I will respond within 24 hours.")
    c.setFont("WSB", 9)
    c.setFillColor(GOLD)
    c.drawString(52, y - 44, "danielolatunji25@gmail.com")

    pg_footer(c, w, 3)
    c.showPage()


# ── MAIN ──────────────────────────────────────────────────────────────────────
c = Canvas.Canvas(OUT, pagesize=A4)
c.setTitle("SME AI Readiness Checklist")
c.setAuthor("Daniel Olatunji | Data & Automation Consultant")
c.setSubject("12 Questions to Assess Your Operations Before Investing in AI")
c.setCreator("Daniel Olatunji Consulting")

cover(c, W, H)
questions_pages(c, W, H)
c.save()
print(f"Done: {OUT}")
