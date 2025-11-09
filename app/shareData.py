
from app.scheduler.botScheduler import BotScheduler
from flask_caching import Cache

class ShareData:
    botScheduler: BotScheduler = None
    app = None
    cache: Cache = None