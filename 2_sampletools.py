import os
from dotenv import load_dotenv
from smolagents import CodeAgent,InferenceClientModel, tool, ToolCallingAgent

load_dotenv()
API_KEY = os.getenv("API_KEY")
print(f"API Key: {API_KEY}")
model = InferenceClientModel (model_id="meta-llama/Llama-3.3-70B-Instruct", token=API_KEY)

@tool
def add_numbers(a: int, b: int) -> int:
    """
    This function takes 2 inputs.
    Args:
        a: First Number.
        b: Second Number.
    Returns:
        Sum of numbers.
    """
    return a + b

# Here we are using ToolCallingAgent  and CodeAgent to call the add_numbers tool. Run both agents in dependently 
# by commenting one after other to see the difference in their behavior.

agent1 = ToolCallingAgent(tools=[add_numbers], model=model, add_base_tools=True)
agent2 = CodeAgent(tools=[add_numbers], model=model, add_base_tools=True)

# Run a simple task
result1 = agent1.run(os.getenv("Sample_tools_Prompt"))
print(result1)

result2 = agent2.run(os.getenv("Sample_tools_Prompt"))
print(result2)
