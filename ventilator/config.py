import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    DEBUG = True if os.environ.get("DEBUG", "False") == "True" else False
    CLIENT_BACKEND = os.environ.get("CLIENT_BACKEND", "discord")
    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
    MEMORY_BACKEND = os.environ.get("MEMORY_BACKEND", "memory")
    LLM_BACKEND = os.environ.get("LLM_BACKEND", "openai")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)


config = Config()
