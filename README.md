━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  AI CONTENT PIPELINE
  Sequential multi-agent workflow — one brief, complete campaign assets.
  by Hans Stewart · hansstewart.dev

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Architecture    →   hansstewart.github.io/ai-architecture
  Portfolio       →   hansstewart.dev
  GitHub          →   github.com/HansStewart/ai-content-pipeline

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A sequential multi-agent content workflow that turns a brief into a
  complete set of campaign assets across multiple channels in a single
  pipeline run.

  Provide a topic, target audience, and tone. The pipeline runs a
  CrewAI-orchestrated chain — Researcher, Copywriter/Editor, Formatter —
  where each agent inherits the full output of the last. The result is
  a unified, multi-channel content package with a consistent strategic
  voice across email, social, blog, and paid copy.

  Use case: rapid campaign production with one structured prompt.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND WORKFLOW — 4 STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step 01 — Brief intake
    Receives a topic, target audience, and tone profile.
    Validates required fields and standardizes the brief structure.
    Initializes the CrewAI run context used by each downstream agent.
    → Input: Topic · audience · tone

  Step 02 — Researcher agent
    Identifies pain points, messaging angles, and audience motivations.
    Creates a structured insight layer that all downstream agents inherit.
    Feeds a clean strategy context into copy generation.
    → Intermediate: Angle map + research context

  Step 03 — Copywriter and editor
    Creates email copy, LinkedIn content, blog outline, and ad variations.
    Runs editorial refinement for clarity, persuasion, and tone alignment.
    Preserves channel-specific formatting while maintaining one strategic
    voice.
    → Processing: Generation + editorial QA

  Step 04 — Formatter agent
    Collects every agent output into one labeled content package.
    Organizes the response into a predictable, publication-ready structure.
    Returns a final bundle through the API for direct operational use.
    → Output: Multi-channel content package


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT CHANNELS PRODUCED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Email copy         Campaign email body, subject line, and CTA
  LinkedIn content   Platform-native post with narrative structure
  Blog outline       SEO-structured post with section breakdown
  Ad variations      Copy variants for paid channel use


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORCHESTRATION MODEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Orchestration    Sequential CrewAI handoff with shared context
                   persistence across all agent roles.
  Consistency      Unified message strategy across all output channels —
                   each agent builds on the last, not from scratch.
  Design pattern   Sequential specialist agents outperform a single
                   undifferentiated one-shot generation step.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  POST /generate
  Content-Type: application/json

  Request
  ───────
  {
    "topic": "...",
    "audience": "...",
    "tone": "..."
  }

  Response
  ────────
  {
    "success": true,
    "content": {
      "email": "...",
      "linkedin": "...",
      "blog_outline": "...",
      "ad_variations": [ "...", "..." ]
    }
  }


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Language        Python 3.11
  Framework       Flask
  Server          Gunicorn
  Orchestration   CrewAI (sequential multi-agent pipeline)
  AI Model        OpenAI GPT-4o
  Deployment      Google Cloud Run — us-east1
  Frontend        Vanilla HTML / CSS / JavaScript


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOCAL DEVELOPMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  git clone https://github.com/HansStewart/ai-content-pipeline.git
  cd ai-content-pipeline
  pip install -r requirements.txt
  cp .env.example .env
  → Add OPENAI_API_KEY to .env
  python main.py
  → Open http://localhost:8080


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
  └── .env.example               OPENAI_API_KEY=


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Hans Stewart · Marketing Automation Engineer · hansstewart.dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━