# AI Content Pipeline

> A sequential multi-agent content workflow that turns a brief into a complete set of campaign assets across multiple channels.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/ai-content-pipeline)

---

## What It Does

Provide a topic, target audience, and tone. The pipeline runs a CrewAI-orchestrated chain — Researcher, Copywriter/Editor, Formatter — where each agent inherits the full output of the last. The result is a unified, multi-channel content package with a consistent strategic voice across email, social, blog, and paid copy.

**Use case:** rapid campaign production with one structured prompt.

---

## Backend Workflow

**Step 1 — Brief intake** `Input: Topic · audience · tone`
Receives a topic, target audience, and tone profile. Validates required fields and standardizes the brief structure. Initializes the CrewAI run context used by each downstream agent.

**Step 2 — Researcher agent** `Intermediate: Angle map + research context`
Identifies pain points, messaging angles, and audience motivations. Creates a structured insight layer that all downstream agents inherit. Feeds a clean strategy context into copy generation.

**Step 3 — Copywriter and editor** `Processing: Generation + editorial QA`
Creates email copy, LinkedIn content, blog outline, and ad variations. Runs editorial refinement for clarity, persuasion, and tone alignment. Preserves channel-specific formatting while maintaining one strategic voice.

**Step 4 — Formatter agent** `Output: Multi-channel content package`
Collects every agent output into one labeled content package. Organizes the response into a predictable, publication-ready structure. Returns a final bundle through the API for direct operational use.

---

## Content Channels Produced

| Channel | Output |
|---|---|
| Email | Campaign email body, subject line, and CTA |
| LinkedIn | Platform-native post with narrative structure |
| Blog | SEO-structured outline with section breakdown |
| Paid | Copy variants for ad use |

---

## Orchestration Model

- **Orchestration** — Sequential CrewAI handoff with shared context persistence across all agent roles.
- **Consistency** — Unified message strategy across all output channels — each agent builds on the last, not from scratch.
- **Design pattern** — Sequential specialist agents outperform a single undifferentiated one-shot generation step.

---

## API Reference

**POST** `/generate`

```json
// Request
{
  "topic": "...",
  "audience": "...",
  "tone": "..."
}

// Response
{
  "success": true,
  "content": {
    "email": "...",
    "linkedin": "...",
    "blog_outline": "...",
    "ad_variations": ["...", "..."]
  }
}
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| Orchestration | CrewAI (sequential multi-agent pipeline) |
| AI Model | OpenAI GPT-4o |
| Deployment | Google Cloud Run — us-east1 |
| Frontend | Vanilla HTML / CSS / JavaScript |

---

## Local Development

```bash
git clone https://github.com/HansStewart/ai-content-pipeline.git
cd ai-content-pipeline
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY to .env
python main.py
# Open http://localhost:8080
```

---

## Project Structure

```
ai-content-pipeline/
├── main.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── agents/
│       ├── researcher.py
│       ├── copywriter.py
│       ├── editor.py
│       └── formatter.py
├── index.html
├── requirements.txt
├── Procfile
└── .env.example          OPENAI_API_KEY=
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | All agent stages and content generation |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| Voice-to-CRM Agent | [github.com/HansStewart/voice-to-crm](https://github.com/HansStewart/voice-to-crm) |
| Pipeline Intelligence Agent | [github.com/HansStewart/pipeline-intelligence-agent](https://github.com/HansStewart/pipeline-intelligence-agent) |
| CRM Automation Agent | [github.com/HansStewart/crm-agent](https://github.com/HansStewart/crm-agent) |
| Multi-Agent BI System | [github.com/HansStewart/multi-agent](https://github.com/HansStewart/multi-agent) |
| AI Data Agent | [github.com/HansStewart/ai-data-agent](https://github.com/HansStewart/ai-data-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**
