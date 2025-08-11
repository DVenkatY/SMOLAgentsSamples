import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
from opentelemetry import trace
from otel_config import configure_otel_for_langfuse

#tracer_provider = trace.get_tracer_provider()
tracer_provider=configure_otel_for_langfuse()
SmolagentsInstrumentor().instrument(tracer_provider=tracer_provider)

load_dotenv()
API_KEY = os.environ.get("API_KEY")
print(f"API Key: {API_KEY}")

model = InferenceClientModel (model_id="meta-llama/Llama-3.3-70B-Instruct", token=API_KEY)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

result = agent.run(os.getenv("Sample_langfuse_Prompt"))

print(result)