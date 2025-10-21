from app.telegram.chatBot import ChatBot
from app.vnstock.stock import StockUtil
from app.utils.messageTemplate import MessageTemplate
from app.utils.excelHelper import ExcelHelper
from vnstock.botbuilder.noti import Messenger
from config import Config

############ Stock price function - start ############
notif = Messenger(platform="telegram", channel=Config.chat_id, token_key=Config.token)

def task_send_notif_stock_price(data):
    stock_code_list = data
    print(f"Executing task_send_notif_stock_price with stock codes: {stock_code_list}")
    
        # notif.send_message(f"Checking stock price for {stock_code}...")
        # latest_price_by_date = StockUtil.get_latest_price_by_date_of_stock(stock_code)
        # current_price = StockUtil.get_current_price_in_real_time(stock_code)
        # print(f"Stock: {stock_code}, Latest Price by Date: {latest_price_by_date}, Current Price: {current_price}")
        # # if current_price greater than 3% or less than 3% of latest_price_by_date, send notification
        # if current_price is None or latest_price_by_date is None:
        #     print(f"Could not fetch prices for {stock_code}. Skipping notification.")
        #     continue
        # if current_price > latest_price_by_date * 1.03:
        #     message = MessageTemplate.stock_price_message(stock_code, latest_price_by_date, current_price)
        #     print(message)
        #     chat_bot.send_message(message)
        # elif current_price < latest_price_by_date * 0.97:
        #     message = MessageTemplate.stock_price_message(stock_code, latest_price_by_date, current_price)
        #     print(message)
        #     chat_bot.send_message(message)

    ############ Stock price function - end ############

mapJobFunction = {
    "task_send_notif_stock_price": task_send_notif_stock_price
}