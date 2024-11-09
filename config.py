import os
from dotenv import load_dotenv

load_dotenv()

# Mistral AI Configuration
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_MODEL = "mistral-tiny"

# Dehashed Configuration
DEHASHED_API_KEY = os.getenv("DEHASHED_API_KEY")
DEHASHED_EMAIL = os.getenv("DEHASHED_EMAIL")

# Chat Configuration
MAX_TOKENS = 1000
TEMPERATURE = 0.7 