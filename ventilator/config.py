import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    DEBUG = True if os.environ.get("DEBUG", "False") == "True" else False
    CLIENT_BACKEND = os.environ.get("CLIENT_BACKEND", "discord")
    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
    MEMORY_BACKEND = os.environ.get("MEMORY_BACKEND", "memory")
    GPT_BACKEND = os.environ.get("GPT_BACKEND", "openai")


config = Config()
