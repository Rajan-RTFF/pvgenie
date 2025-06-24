from crewai import Task

def intake_task(agent):
    return Task(
        description="Ask user for product name, regions where it's marketed, and type of PV system they need (in-house or vendor-managed).",
        agent=agent,
        expected_output="Structured product profile with regions and PV needs."
    )

def regulatory_task(agent):
    return Task(
        description="Based on product profile and markets, list required regulatory obligations and documents (e.g., EU QPPV, PSURs).",
        agent=agent,
        expected_output="List of region-specific PV obligations and document types."
    )

def sop_task(agent):
    return Task(
        description="Generate 2 SOPs: one for case intake and one for literature screening based on regulatory needs.",
        agent=agent,
        expected_output="Two detailed SOP drafts in plain text."
    )
