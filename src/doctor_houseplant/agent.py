from importlib import resources as impresources
from google.adk.agents import LlmAgent
from google.genai import types

# Read the instruction provided with the package
instruction = impresources.read_text(__package__, "INSTRUCTION.md")

# Create our agent config,
# use a low temperature for consistency
# set safety settings to block any dangerous content.
content_config = types.GenerateContentConfig(
    temperature=0.1,  # Very low for consistency
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        )
    ],
)

# Create the agent with the instruction and other metadata.
doctor_houseplant = LlmAgent(
    model="gemini-2.5-flash",
    name="doctor_houseplant",  # Used by ADK internally
    description="Identifies plants and helps taking care of them.",
    instruction=instruction,
    generate_content_config=content_config,
)

# Variable name that ADK tools look for (must be root_agent)
root_agent = doctor_houseplant
