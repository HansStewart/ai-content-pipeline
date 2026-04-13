# 🤖 AI Content Pipeline Agent

A 4-agent CrewAI pipeline that takes a topic, target audience, and tone as inputs and produces a complete content package in one run — email campaign, LinkedIn post, blog outline, and ad copy variations.

**Live API:** https://ai-content-pipeline-559169459241.us-east1.run.app

---

## Agent Pipeline
Input: Topic · Audience · Tone
│
▼
┌─────────────────────────────────┐
│ Agent 1 — Researcher │
│ Identifies angles · pain pts │
│ audience motivations │
└─────────────┬───────────────────┘
│
▼
┌─────────────────────────────────┐
│ Agent 2 — Copywriter │
│ Email · LinkedIn · Blog │
│ Outline · 3 Ad Variations │
└─────────────┬───────────────────┘
│
▼
┌─────────────────────────────────┐
│ Agent 3 — Editor │
│ Clarity · Persuasion · Flow │
│ Tone consistency │
└─────────────┬───────────────────┘
│
▼
┌─────────────────────────────────┐
│ Agent 4 — Formatter │
│ Final labeled content package │
│ Ready to publish immediately │
└─────────────────────────────────┘

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent Framework | CrewAI 0.11.2 |
| AI / LLM | OpenAI GPT-4o |
| Web Framework | Flask 3.1 + Gunicorn |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |

---

## API Reference

### `GET /`
Health check.

### `POST /generate`
Generate a full content package.

**Request:**
```json
{
  "topic": "AI automation for small businesses",
  "audience": "small business owners",
  "tone": "professional"
}
```

**Response:**
```json
{
  "success": true,
  "inputs": { "topic": "...", "audience": "...", "tone": "..." },
  "content_package": "RESEARCH SUMMARY\n...\nEMAIL CAMPAIGN\n...\nLINKEDIN POST\n...\nBLOG OUTLINE\n...\nAD COPY VARIATIONS\n..."
}
```