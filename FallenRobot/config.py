import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "1234"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DATABASE_URL = os.environ.get("DATABASE_URL")
