from crewai import Crew
from intake_agent import intake_agent
from regulatory_agent import regulatory_agent
from sop_agent import sop_agent
from tasks import intake_task, regulatory_task, sop_task

def build_crew():
    crew = Crew(
        agents=[intake_agent, regulatory_agent, sop_agent],
        tasks=[
            intake_task(intake_agent),
            regulatory_task(regulatory_agent),
            sop_task(sop_agent)
        ],
        verbose=True
    )
    return crew
