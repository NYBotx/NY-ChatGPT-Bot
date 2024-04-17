import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "19911978"))
API_HASH = environ.get("API_HASH", "e3f5848d4c384af9e6f1f52ca84c19c7")
BOT_TOKEN = environ.get("BOT_TOKEN", "7097497120:AAHgCulZw3AYU2pTFZ5L3rsGK5VNXM62inI")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002081616844"))
ADMINS = int(environ.get("ADMINS", ""))
DB_URI = environ.get("DB_URI", "mongodb+srv://nischay419:nischay419@cluster0.z6hynou.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptnybot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
