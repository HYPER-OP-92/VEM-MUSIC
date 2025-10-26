from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", ""))
        self.API_HASH = getenv("API_HASH", "")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "")
        self.MONGO_URL = getenv("MONGO_URL", "")

        self.LOGGER_ID = int(getenv("LOGGER_ID", ""))
        self.OWNER_ID = int(getenv("OWNER_ID", ""))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_ABOUT_VENOM_ll")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://graph.org/file/6b30206fe580579f7901b-22e97987d6810abb7a.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://graph.org/file/d42fe8b7d886eec1f3861-245c868a9b1a52da72.jpg")
        self.START_IMG = getenv("START_IMG", "https://graph.org/file/9abcd08f983ba23bd86f1-a98312e4e8f82bb03b.jpg")
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
