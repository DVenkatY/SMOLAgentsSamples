import os
import base64
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter


def configure_otel_for_langfuse():
    """Configures OpenTelemetry to export traces to Langfuse."""
    # Set up Langfuse API keys as environment variables
    # Replace with your actual keys or load from environment
    LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
    LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")

    if not LANGFUSE_PUBLIC_KEY or not LANGFUSE_SECRET_KEY:
        raise ValueError("Langfuse API keys not set in environment variables.")

    LANGFUSE_AUTH = base64.b64encode(f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}".encode()).decode()


    os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "http://us.cloud.langfuse.com/api/public/otel"
    os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"
    
    # Configure tracer provider
    trace_provider = TracerProvider()
    trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))

    print("OpenTelemetry configured for Langfuse export.")
    return trace_provider  # Return the tracer provider for further use