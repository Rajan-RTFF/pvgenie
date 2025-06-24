from crewai import Agent

intake_agent = Agent(
    role="Intake Agent",
    goal="Collect PV-relevant data about the client’s product and market.",
    backstory="You are responsible for gathering key information like regions of market, type of product, and reporting obligations.",
    verbose=True
)
