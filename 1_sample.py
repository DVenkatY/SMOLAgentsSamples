import os
from dotenv import load_dotenv
from smolagents import CodeAgent,InferenceClientModel 

load_dotenv()
API_KEY = os.getenv("API_KEY")
print(f"API Key: {API_KEY}")

model = InferenceClientModel (model_id="meta-llama/Llama-3.3-70B-Instruct", token=API_KEY)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

# Run a simple task
result = agent.run(os.getenv("Sample_Prompt"))
print(result)