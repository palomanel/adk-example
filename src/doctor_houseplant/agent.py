from importlib import resources as impresources
from google.adk.agents.llm_agent import Agent

# Read the instruction provided with the package
instruction = impresources.read_text(__package__, "INSTRUCTION.md")

# Create the agent with the instruction and other metadata.
doctor_houseplant = Agent(
    model="gemini-2.5-flash",
    name="doctor_houseplant",  # Used by ADK internally
    description="Identifies plants and helps taking care of them.",
    instruction=instruction,
)

# Variable name that ADK tools look for (must be root_agent)
root_agent = doctor_houseplant
