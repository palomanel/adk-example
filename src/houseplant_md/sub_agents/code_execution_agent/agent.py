"""
Code Execution Agent

Perform tasks like calculations, data manipulation, or
running small scripts.
"""

from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

CodeExecutionAgent = LlmAgent(
    name="code_execution_agent",
    description="Execute code and perform computations.",
    model="gemini-2.5-flash",
    instruction="You help users with calculations and data processing.",
    # Enable code execution
    code_executor=BuiltInCodeExecutor(),
)
