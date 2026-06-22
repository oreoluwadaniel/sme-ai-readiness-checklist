# SME AI Readiness Checklist

**A free, downloadable PDF resource for SME leaders and operations managers.**

Before any business invests time or money in AI tools, there are 12 questions that need honest answers. Not about technology. About operations.

This checklist gives you a structured way to assess your current state across three operational layers, score your readiness, and understand exactly where to start.

---

## What is inside

A professionally designed 3-page PDF that covers:

- **12 diagnostic questions** across three operational layers
- **A scoring guide** that translates your total into a clear starting point
- **"Why this matters" context** for every question, written for operations people, not engineers

---

## The Three-Layer Framework

The checklist is built around a systems-based approach to AI integration. Businesses that successfully adopt AI do not do it all at once. They work in layers.

### Layer 1: Visibility

Before you automate anything, you need to see what is actually happening in your business. This means consolidating your data into one place, whether that is a simple dashboard, a CRM, or a reporting tool. The goal is not sophistication. It is clarity.

Sample questions from this layer:
- Do you have a single source of truth for your customer data?
- Can your team describe your top three operational bottlenecks in under 60 seconds?
- Do your operations team and finance team work from the same numbers each week?

### Layer 2: Automation

Once you can see the patterns, you start automating the repetitive decisions. Invoice routing. Lead scoring. Follow-up sequences. Stock level alerts. These are tasks where the logic is already known but is being executed manually.

Sample questions from this layer:
- Do you know your average cost per manual process?
- Are there tasks your team performs the same way every single day without variation?
- Could a new team member follow a written process for your five most repeated tasks?

### Layer 3: Intelligence

When your data is clean and your routine tasks are automated, you apply AI to decisions that previously required experience. Forecasting demand. Identifying which leads are most likely to convert. Flagging expenses trending in the wrong direction before the month is over.

Sample questions from this layer:
- Do you have at least 12 months of clean, structured historical data in one place?
- Does your team trust data enough to make decisions without calling a verification meeting?
- Do you have one named person responsible for data quality in your business?

---

## Scoring Guide

Score one point for every YES. No partial credit.

| Score | What it means | Where to start |
|-------|--------------|----------------|
| 0 to 4 | You need visibility first | Build a single dashboard your whole team checks weekly |
| 5 to 8 | You are ready to automate | Document your top 3 manual processes and find the right tool |
| 9 to 12 | You are ready for intelligence | Apply AI to forecasting, churn prediction, and spend analysis |

---

## Download the PDF

The finished checklist PDF is available in the `/output` folder of this repository:

[**Download: AI_Readiness_Checklist_Daniel_Olatunji.pdf**](./output/AI_Readiness_Checklist_Daniel_Olatunji.pdf)

---

## Generate it yourself

If you want to regenerate or customise the PDF, it is built entirely in Python using ReportLab.

### Requirements

```
Python 3.8+
reportlab
```

### Install dependencies

```bash
pip install reportlab
```

### Run the generator

```bash
python generate_checklist.py
```

The PDF will be saved to the `/output` folder.

### Fonts used

The script uses these open-licence fonts, included in the `/fonts` folder:

- Work Sans (Regular, Bold, Italic)
- IBM Plex Serif (Regular, Bold, Italic)

---

## Who this is for

This checklist is aimed at:

- SME founders and CEOs evaluating whether AI is right for their business right now
- Operations managers who want a structured way to assess process maturity
- Finance and commercial leads who need to understand what AI readiness actually means before signing off on tools

It is not a pitch for any specific AI product. It is a diagnostic. Use it to understand where you are before deciding where to go.

---

## About

Created by **Daniel Olatunji**, Data and Automation Consultant.

I work with early-stage founders and SME operators across Africa, the UK, and Europe to replace manual reporting and disconnected systems with clean data infrastructure and automated workflows.

If you want to talk through your score or understand what the next step looks like for your specific business, reach out at **danielolatunji25@gmail.com**.

---

## Licence

This resource is free to download, share, and reference. You are welcome to adapt the framework for your own use. If you redistribute it, please credit the original.

---

## Repository structure

```
/
├── README.md
├── generate_checklist.py
├── requirements.txt
├── output/
│   └── AI_Readiness_Checklist_Daniel_Olatunji.pdf
├── fonts/
│   ├── WorkSans-Regular.ttf
│   ├── WorkSans-Bold.ttf
│   ├── WorkSans-Italic.ttf
│   ├── IBMPlexSerif-Regular.ttf
│   ├── IBMPlexSerif-Bold.ttf
│   └── IBMPlexSerif-Italic.ttf
└── .gitignore
```
