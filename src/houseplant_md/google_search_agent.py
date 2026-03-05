"""
Google Search Agent

Use the Google Search tool to answer questions based on factual information.

When using Google Search grounding, you MUST display search suggestions
(renderedContent) in your application UI. This is mandatory per Google
Search usage policy.
"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

GoogleSearchAgent = LlmAgent(
    name="google_search_agent",
    description="Answer questions using Google Search.",
    model="gemini-2.5-flash",
    instruction="You are an expert researcher. You stick to the facts.",
    # Add the built-in google_search tool to the agent's toolset
    tools=[google_search],
)
