from crewai import Agent

sop_agent = Agent(
    role="SOP Generator Agent",
    goal="Generate SOPs for case intake and literature search based on regulatory needs.",
    backstory="You write tailored SOPs for pharmacovigilance operations.",
    verbose=True
)
