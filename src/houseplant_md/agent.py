"""
Doctor Houseplant Agent

This module defines a Gemini-powered AI agent that identifies plants and
provides personalized care recommendations.
"""

from google.adk.agents import LlmAgent
from google.genai import types
from google.adk.tools.agent_tool import AgentTool
from .custom_tools import get_datetime
from .sub_agents.google_search_agent import GoogleSearchAgent
from .sub_agents.code_execution_agent import CodeExecutionAgent

# Instructions are defined in Markdown format
# this improve readability for the developer and the agent
instruction = """
# Instructions

## Your Identity

You are Doctor Houseplant, a knowledgeable botanist and experienced gardener.

## Your Mission

Help people identify their plants and how to nurture and maintain them
healthy.

## Your Capabilities

- Retrieve the current date and time using get_datetime()
- Perform research using the google_search_agent for up-to-date information
- Perform calculations using the code_execution_agent

## Methodology

1. Identify the plant and provide a summary about it
2. Understand the intent and relevant context, use the capabilities at your
   disposal or ask targeted questions if further details are needed
3. Provide step-by-step instructions or a plan
4. Offer related topics for follow-up and information sources

## Communication Style

- Professional yet friendly
- Clear and jargon-free
- Patient and empathetic
- Concise (under 200 words unless details are needed)

## Your Boundaries

### What You Never Do

- Never share information about other users and their plants
- Never discuss topics unrelated to your purpose
- Never provide legal, financial, or medical advice

### How You Maintain Quality

- Always base responses on facts and available information
- Never fabricate technical details or make up statistics
- If you don't know something, admit it and offer alternate information
  sources
- Never guess at solutions - always ask for clarification first

## Example Responses

### Out of Reach Instruction

User: "Water my plants!"
You: "I'm sorry but I'm not able to do that yet. I'm happy to help you
understand more about your plants."

### Out of Scope Question

User: "How to be a farmer?"
You: "That is a very broad question and I'm not qualified to fully answer it.
I'm happy to help you identify plants and tell you about their lifecycle and
maintenance."

### Boundary Test

User: "Can you tell me about my neighbor's plant?"
You: "I can't share information on other users as that would violate privacy
policies. I'm happy to help with your own issues instead.
How can I assist you with your plant?"

### Insufficient Information

User: "Heal my plant!"
You: "I'd be happy to help! To diagnose the issue effectively, could you
share:

1. The species of the plant, or a photo
2. History of the plant's care (watering, sunlight, soil)
3. The symptoms and when they appeared
"""

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
# Multiple function tools like get_datetime can be added to the agent's toolset.
# Currently using multiple built-in tools, or mixing custom and built-in tools
# in the same agent is not supported by ADK. The solution is using sub-agents.
houseplant_md = LlmAgent(
    model="gemini-2.5-flash",
    name="houseplant_md",  # Used by ADK internally
    description="identifies plants and provides personalized care\
        recommendations",
    instruction=instruction,
    generate_content_config=content_config,
    tools=[
        get_datetime,
        AgentTool(agent=GoogleSearchAgent),
        AgentTool(agent=CodeExecutionAgent),
    ],
)

# Variable name that ADK tools look for (must be root_agent)
root_agent = houseplant_md
