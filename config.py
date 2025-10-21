from apscheduler.schedulers.background import BackgroundScheduler
class Config:
    token = "8466290247:AAGh_Jy9F0nuwOW6_YoPvxcJFUvImSJygLE"
    chat_id = "-4933195267"
    scheduler : BackgroundScheduler = None
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@103.146.23.178:3306/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
