from apscheduler.schedulers.background import BackgroundScheduler

PAGE_FB_TOKEN = "EAAyxihCe66sBPZC1g803vz17U9VHCAwkRCCH2cHqMIH7yx8PsuOLPKu5POKzygqkdhWJmTD6cXONOcwZCu1cBFi0MaBqclB6QkNgzCJr6oc7um1ygciTrhUZCaIHykl7THXJki0IMZC2SX0DEEVvwyLPOCl8P5XsbQpKCrq5RKoTf4NEhmwZAtqDtRjNJGmRxD02wlJcn"
class Config:
    token = "8466290247:AAGh_Jy9F0nuwOW6_YoPvxcJFUvImSJygLE"
    chat_id = "-4933195267"
    scheduler : BackgroundScheduler = None
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@103.146.23.178:3306/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
