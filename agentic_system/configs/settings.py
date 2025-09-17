
import os
from openai import OpenAI
from dotenv import load_dotenv
import os
from agents import set_default_openai_client
from openai import AsyncAzureOpenAI

# Load environment variables from .env file (if you use one)
load_dotenv()

OPENAI_API_KEY = "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"



class Settings:
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION", "v1")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-nano")

    openai_client = OpenAI(
        api_key=OPENAI_API_KEY,
        # base_url=OPENAI_API_BASE,
    )

    GEMINI_API_KEY = "AIzaSyBtFwcFIW3MNsls3xmrnr4RDCUIK4NTjDQ"


settings = Settings()


# def check_config():
#     if not all([settings.OPENAI_API_KEY, settings.AZURE_AI_SEARCH_ENDPOINT, settings.AZURE_AI_SEARCH_KEY, settings.AZURE_AI_SEARCH_INDEX]):
#         raise ValueError("One or more required environment variables are not set. Please check your .env file.")


