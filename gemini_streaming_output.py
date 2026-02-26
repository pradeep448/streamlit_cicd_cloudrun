#pip install google-genai
#pip install google-auth

from google.genai import Client

PROJECT_ID =  "<YOUR-GCP-PROJECT-ID>"
REGION = "us-central1"
MODEL_NAME = "gemini-2.0-flash-001"

client = Client(
    vertexai=True,
    project=PROJECT_ID,
    location=REGION,
)

responses = client.models.generate_content_stream(
    model=MODEL_NAME,
    contents="Can you write a poem of 400 lines on earth",
)
for chunk in responses:
    # Each 'chunk' is a GenerationResponse or similar object containing parts.
    # For text-only responses, 'chunk.text' is the easiest way to get the text.
    print(chunk.text, end="", flush=True)