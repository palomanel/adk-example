from google.adk.agents.llm_agent import Agent

math_tutor_agent = Agent(
    model="gemini-2.5-flash",
    name="math_tutor_agent",  # Used by ADK internally
    description="Helps students with algebra",
    instruction="You are a patient math tutor who helps students understand\
                 algebra concepts. You provide clear explanations and\
                 step-by-step solutions to problems.",
)

# Variable name that ADK tools look for (must be root_agent)
root_agent = math_tutor_agent
