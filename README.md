🤖 AI Content Pipeline Agent
==============================

A 4-agent CrewAI pipeline that takes a topic, target audience, and tone as inputs and produces a complete content package in one run — email campaign, LinkedIn post, blog outline, and ad copy variations.

🌐 Live API: [https://ai-content-pipeline-559169459241.us-east1.run.app](https://ai-content-pipeline-559169459241.us-east1.run.app)



🔁 Agent Pipeline
------------------

```
Input: Topic · Audience · Tone
│
▼
┌─────────────────────────────────┐
│  Agent 1 — Researcher           │
│  Identifies angles · pain pts   │
│  audience motivations           │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Agent 2 — Copywriter           │
│  Email · LinkedIn · Blog        │
│  Outline · 3 Ad Variations      │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Agent 3 — Editor               │
│  Clarity · Persuasion · Flow    │
│  Tone consistency               │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│  Agent 4 — Formatter            │
│  Final labeled content package  │
│  Ready to publish immediately   │
└─────────────────────────────────┘
```



📦 Overview
------------

The AI Content Pipeline Agent automates the full content creation workflow using a team of four specialized AI agents built on CrewAI. Each agent has a defined role and passes its output to the next — from research to copywriting to editing to final formatting — producing a publication-ready content package in a single API call.



✨ Features
-----------

- Four chained AI agents each with a distinct role in the content creation process
- Researcher agent identifies topic angles, pain points, and audience motivations
- Copywriter agent produces a full email campaign, LinkedIn post, blog outline, and three ad copy variations
- Editor agent reviews for clarity, persuasion, flow, and tone consistency
- Formatter agent delivers a clean, labeled content package ready to publish
- Single POST request triggers the full pipeline end to end
- Containerized with Docker and deployed on Google Cloud Run
- Health check endpoint for uptime monitoring



🛠 Tech Stack
--------------

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent Framework | CrewAI 0.11.2 |
| AI / LLM | OpenAI GPT-4o |
| Web Framework | Flask 3.1 + Gunicorn |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |



📁 Project Structure
---------------------

```
ai-content-pipeline/
├── app.py                  Flask app — routes and request handling
├── agents.py               CrewAI agent definitions — Researcher, Copywriter, Editor, Formatter
├── tasks.py                Task definitions assigned to each agent
├── crew.py                 CrewAI pipeline orchestration
├── requirements.txt        Python dependencies
├── Dockerfile              Container configuration
├── .dockerignore           Files excluded from Docker build
├── .env                    Local environment variables (never committed)
├── .env.example            Environment variable template for contributors
└── .gitignore              Git exclusions
```



⚙️ Setup and Installation
--------------------------

Prerequisites:

- Python 3.11+
- Git
- Docker (for containerized deployment)
- Google Cloud SDK (for Cloud Run deployment)
- OpenAI API key

1. Clone the Repository

```bash
git clone https://github.com/HansStewart/ai-content-pipeline.git
cd ai-content-pipeline
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
source venv/bin/activate        # macOS / Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and set your values:

```
OPENAI_API_KEY=your_openai_api_key_here
```



▶️ Running Locally
-------------------

```bash
python app.py
```

The server will start at:

```
http://localhost:8080
```



🐳 Running with Docker
-----------------------

```bash
docker build -t ai-content-pipeline .
docker run -p 8080:8080 --env-file .env ai-content-pipeline
```



☁️ Deploying to Google Cloud Run
----------------------------------

Deploy from Source:

```bash
gcloud run deploy ai-content-pipeline \
  --source . \
  --region us-east1 \
  --platform managed \
  --allow-unauthenticated \
  --timeout 300
```

Set Environment Variables:

```bash
gcloud run services update ai-content-pipeline \
  --region us-east1 \
  --set-env-vars OPENAI_API_KEY=your_key_here
```



🔌 API Reference
-----------------

GET /

Health check.

POST /generate

Generate a full content package.

Request:

```json
{
  "topic": "AI automation for small businesses",
  "audience": "small business owners",
  "tone": "professional"
}
```

Response:

```json
{
  "success": true,
  "inputs": {
    "topic": "AI automation for small businesses",
    "audience": "small business owners",
    "tone": "professional"
  },
  "content_package": "RESEARCH SUMMARY\n...\nEMAIL CAMPAIGN\n...\nLINKEDIN POST\n...\nBLOG OUTLINE\n...\nAD COPY VARIATIONS\n..."
}
```



📤 Content Package Output
--------------------------

Each successful run returns a labeled content package containing:

- Research Summary — key angles, pain points, and audience motivations
- Email Campaign — subject line, preview text, and full body copy
- LinkedIn Post — hook, body, and call to action formatted for LinkedIn
- Blog Outline — title, introduction, section headers, and conclusion notes
- Ad Copy Variations — three distinct ad copy versions with different angles



🔐 Security Notes
------------------

- Never commit your .env file — it is excluded via .gitignore
- Use Google Cloud Secret Manager for production-grade secret management
- Cloud Run services can be restricted to authenticated access by removing --allow-unauthenticated



🗺 Roadmap
-----------

- Add support for custom tone presets saved per client
- Add Twitter/X thread format as a fifth content output
- Add a web UI for non-technical users to submit requests
- Integrate with HubSpot to auto-load generated emails into campaigns
- Add webhook support to trigger the pipeline from external tools like n8n or Zapier



👤 Author
----------

Hans Stewart

[GitHub](https://github.com/HansStewart)



Built with Python, CrewAI, OpenAI GPT-4o, and Google Cloud Run.