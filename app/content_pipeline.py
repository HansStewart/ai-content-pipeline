import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def _gpt(system_prompt, user_prompt, model="gpt-4o", max_tokens=4096, temperature=0.75):
    """Direct OpenAI call — no crewai, no agent theatrics."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def run_content_pipeline(topic, audience, tone, business_name="", business_type="",
                         key_message="", format_block="", outputs=None):
    if outputs is None:
        outputs = []

    brief = f"""
Business: {business_name}
Business Type: {business_type}
Topic / Campaign: {topic}
Target Audience: {audience}
Tone / Voice: {tone}
Key Message or Offer: {key_message if key_message else "Not specified"}
""".strip()

    # ── Step 1: Research ────────────────────────────────────────────────────
    research = _gpt(
        system_prompt="""You are a senior content strategist and audience researcher. 
Analyze the campaign brief and return a detailed research summary covering:
- Top 3 audience pain points
- Key motivations and desires
- 3 strong messaging angles
- Differentiators to emphasize
- Recommended hooks and CTAs
Be specific and actionable.""",
        user_prompt=brief,
        max_tokens=800,
        temperature=0.6,
    )

    # ── Step 2: Write every format ──────────────────────────────────────────
    write_system = f"""You are an elite direct-response copywriter with 20 years of experience.

You write COMPLETE, FULLY WRITTEN marketing content — every word final and publish-ready.

ABSOLUTE RULES:
- Write every format in FULL — no outlines, no placeholders, no summaries
- Blog posts: minimum 1,200 words of actual body content
- Guides: minimum 1,500 words of actual body content  
- Each email: minimum 200 words of actual body copy
- Do NOT use [brackets] as placeholders — write the actual words
- Do NOT say "write X here" — write it yourself

Campaign Brief:
{brief}

Research Summary:
{research}

Write for this audience in a {tone} voice."""

    write_prompt = f"""Write COMPLETE, FULLY WRITTEN content for every format below.
Every format must be 100% finished copy, ready to publish RIGHT NOW.

{format_block}

Output each format using EXACTLY this separator:
=== FORMAT_NAME ===
[complete content]

Use the exact format names as labels (e.g. instagram, facebook, blog, email_campaign, etc.)"""

    raw_content = _gpt(
        system_prompt=write_system,
        user_prompt=write_prompt,
        max_tokens=4096,
        temperature=0.8,
    )

    # ── Step 3: If content looks truncated, continue generating ─────────────
    word_count = len(raw_content.split())
    if word_count < 300 and len(outputs) > 0:
        # Content was cut off — generate each format individually
        sections = []
        for fmt in outputs:
            if fmt == "images":
                continue
            fmt_system = f"""You are an elite direct-response copywriter.
Write COMPLETE, FULLY WRITTEN content for ONE format.
Campaign: {brief}
Research: {research}
Tone: {tone}
Write every word as final, publish-ready copy. No placeholders. No outlines."""

            from app import FORMAT_GUIDE
            fmt_instruction = FORMAT_GUIDE.get(fmt, f"Write compelling {fmt} content.")
            fmt_content = _gpt(
                system_prompt=fmt_system,
                user_prompt=f"Write this format in FULL:\n\n{fmt_instruction}",
                max_tokens=4096,
                temperature=0.8,
            )
            sections.append(f"=== {fmt} ===\n{fmt_content}")
        raw_content = "\n\n".join(sections)

    # ── Step 4: Format / clean up output ────────────────────────────────────
    format_system = """You are a content formatter. Your ONLY job is to take the content provided 
and reformat it cleanly using === FORMAT_NAME === markers.

RULES:
- Output the COMPLETE FULL TEXT of every section — do not shorten anything
- Do NOT add commentary or review notes
- Do NOT say anything about the content quality
- Keep every single word of the original content
- Just clean up the section markers to match the exact format names provided"""

    format_prompt = f"""Reformat this content. Keep every word. Just ensure each section uses
the exact === FORMAT_NAME === marker format.

Format names to use: {", ".join([o for o in outputs if o != "images"])}

Content to format:
{raw_content}"""

    final = _gpt(
        system_prompt=format_system,
        user_prompt=format_prompt,
        max_tokens=4096,
        temperature=0.2,
    )

    return final