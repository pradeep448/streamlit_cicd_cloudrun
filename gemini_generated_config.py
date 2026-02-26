#pip install google-genai
#pip install google-auth

from google.genai import Client
from google.genai import types
from google.genai.types import HarmCategory, HarmBlockThreshold

PROJECT_ID =  "<YOUR-GCP-PROJECT-ID>"
REGION = "us-central1"
MODEL_NAME = "gemini-2.0-flash-001"

client = Client(
    vertexai=True,
    project=PROJECT_ID,
    location=REGION,
)

generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 655,
    safety_settings = [types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=None
    ),types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    ),types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=None
    )],
    thinking_config=types.ThinkingConfig(
      thinking_budget=0,
    ),
  )

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="What is the color of Apple",
    config= generate_content_config,
)

print("Model Response:\n", response.text)