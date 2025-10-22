from app.bot.botTelegram import ChatBot
from app.vnstock.stock import StockUtil
from app.utils.messageTemplate import MessageTemplate
from app.utils.excelHelper import ExcelHelper
# from vnstock.botbuilder.noti import Messenger
import os
import ast
from app.model.notifcationLogRepo import add_notification_log, is_sent_notif_today
from app.bot import botFacebook
############ Stock price function - start ############
# notif = Messenger(platform="telegram", channel=Config.chat_id, token_key=Config.token)
chatBot = ChatBot(token=os.getenv('TELEGRAM_TOKEN'), chat_id=os.getenv('TELEGRAM_CHAT_ID'))
def task_send_notif_stock_price(data):
    stock_code_list = ast.literal_eval(data)
    print(f"Executing task_send_notif_stock_price with stock codes: {stock_code_list}")
    for stock_code in stock_code_list:
        print(f"Preparing to check stock price for {stock_code}...")
        latest_price_by_date = StockUtil.get_latest_price_by_date_of_stock(stock_code)
        current_price = StockUtil.get_current_price_in_real_time(stock_code)
        print(f"Stock: {stock_code}, Latest Price by Date: {latest_price_by_date}, Current Price: {current_price}")
        # if current_price greater than 3% or less than 3% of latest_price_by_date, send notification
        if current_price is None or latest_price_by_date is None:
            print(f"Could not fetch prices for {stock_code}. Skipping notification.")
            continue
        if current_price > latest_price_by_date * 1.03:
            message = MessageTemplate.stock_price_message(stock_code, latest_price_by_date, current_price)
            if is_sent_notif_today(platform="telegram", channel=chatBot.chat_id, stock_code=stock_code):
                print(f"Notification for {stock_code} already sent today. Skipping.")
                continue
            else:
                add_notification_log(platform="telegram", channel=chatBot.chat_id, message=message, stock_code=stock_code)
                chatBot.send_message(message)
                print(botFacebook.send_message(message_text=message))
                add_notification_log(platform="facebook", channel=botFacebook.RECIPIENT_IDS[0], message=message, stock_code=stock_code)
        elif current_price < latest_price_by_date * 0.97:
            message = MessageTemplate.stock_price_message(stock_code, latest_price_by_date, current_price)
            if is_sent_notif_today(platform="telegram", channel=chatBot.chat_id, stock_code=stock_code):
                print(f"Notification for {stock_code} already sent today. Skipping.")
                continue
            else:
                add_notification_log(platform="telegram", channel=chatBot.chat_id, message=message, stock_code=stock_code)
                chatBot.send_message(message)
                botFacebook.send_message(message_text=message)
                add_notification_log(platform="facebook", channel=botFacebook.RECIPIENT_IDS[0], message=message, stock_code=stock_code)

    ############ Stock price function - end ############

mapJobFunction = {
    "task_send_notif_stock_price": task_send_notif_stock_price
}