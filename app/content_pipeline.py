import os
from crewai import Agent, Task, Crew
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_content_pipeline(topic, audience, tone):
    researcher = Agent(
        role="Content Researcher",
        goal="Research the topic and identify the strongest messaging angles for the target audience.",
        backstory="You specialize in audience research, positioning, and identifying the most relevant ideas for marketing content.",
        verbose=True
    )

    copywriter = Agent(
        role="Marketing Copywriter",
        goal="Write compelling marketing content tailored to the audience and tone.",
        backstory="You create clear, persuasive copy for emails, social posts, and ads.",
        verbose=True
    )

    editor = Agent(
        role="Content Editor",
        goal="Improve clarity, consistency, tone, and quality across all content pieces.",
        backstory="You refine drafts so they are polished, on-brand, and ready to publish.",
        verbose=True
    )

    formatter = Agent(
        role="Content Formatter",
        goal="Structure the final content package into clearly labeled sections.",
        backstory="You prepare content deliverables so they are easy for teams to use immediately.",
        verbose=True
    )

    research_task = Task(
        description=f"Research the topic '{topic}' for the audience '{audience}' with a '{tone}' tone. Identify key pain points, motivations, and strong messaging angles.",
        expected_output="A concise research summary with audience insights and messaging direction.",
        agent=researcher
    )

    writing_task = Task(
        description=f"Using the research, write: 1) one marketing email, 2) one LinkedIn post, 3) one blog outline, and 4) three ad copy variations for the topic '{topic}', audience '{audience}', and tone '{tone}'.",
        expected_output="A draft email, LinkedIn post, blog outline, and 3 ad variations.",
        agent=copywriter
    )

    editing_task = Task(
        description="Edit the written content for clarity, persuasion, flow, and tone consistency.",
        expected_output="An improved version of all content pieces with stronger readability and messaging.",
        agent=editor
    )

    formatting_task = Task(
        description="Format the final content into these exact sections: Research Summary, Email Campaign, LinkedIn Post, Blog Outline, Ad Copy Variations.",
        expected_output="A final content package with clearly separated sections and polished output.",
        agent=formatter
    )

    crew = Crew(
        agents=[researcher, copywriter, editor, formatter],
        tasks=[research_task, writing_task, editing_task, formatting_task],
        verbose=True
    )

    result = crew.kickoff()
    return str(result)