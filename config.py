import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    AUTH_USERS = [int(user) for user in os.getenv("AUTH_USERS").split(",")]