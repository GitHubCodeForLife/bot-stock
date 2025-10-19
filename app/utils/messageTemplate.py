from datetime import datetime, timedelta  

class MessageTemplate: 
    @staticmethod
    def stock_price_message(stock_code, price, date = None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        message = f"#{stock_code} Price Update\n"
        message += f"Date: {date}\n"
        message += f"Latest Price: {price} VND"
        return message
