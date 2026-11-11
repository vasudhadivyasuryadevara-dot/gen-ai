
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(override=True)

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# List available Gemini models
print("\n===== AVAILABLE GEMINI MODELS =====\n")

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)
