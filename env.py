import os
 
 
class EnvData:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # from @botfather
    API_ID = os.environ.get("API_ID", "") # your api id from my.telegram.org. Sample :- int("123456")
    API_HASH = os.environ.get("API_HASH", "") # your api hash from my.telegram.org Sample :- "fayasnoushad123"
