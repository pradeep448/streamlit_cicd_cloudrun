#pip install google-genai
#pip install google-auth

from google.genai import Client
from google.oauth2.service_account import Credentials
api_key_path = "<PATH-TO-YOUR-KEY-FILE>"

credentials = Credentials.from_service_account_file(
    api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

PROJECT_ID =  "<YOUR-GCP-PROJECT-ID>"
REGION = "us-central1"
MODEL_NAME = "gemini-2.0-flash-001"

client = Client(
    vertexai=True,
    project=PROJECT_ID,
    location=REGION,
    credentials=credentials
)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="What is the color of Apple?"
)

print("Model Response:\n", response.text)
