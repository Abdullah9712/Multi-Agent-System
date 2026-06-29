import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Default Gemini Model
MODEL_NAME ="gemini-2.5-flash"