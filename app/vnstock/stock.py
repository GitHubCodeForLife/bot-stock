from vnstock import Vnstock
from datetime import datetime, timedelta 

class StockUtil:
    @staticmethod
    def get_start_price_of_day(stock_code, date=None):
        try:
            stock = Vnstock().stock(symbol=stock_code, source='VCI')
            if date is None:
                date = datetime.now().strftime("%Y-%m-%d")
            today = datetime.strptime(date, "%Y-%m-%d")
            
            df = stock.quote.history(
                start=today.strftime("%Y-%m-%d"),
                end=today.strftime("%Y-%m-%d"),
                interval='1D'
            )

            if df.empty:
                print("No data found for the given date range.")
                return None
    
            start_price = df.tail(1)['close'].values[0]
            return start_price

        except Exception as e:
            print(f"Error fetching stock price: {e}")
            return None
        
    @staticmethod 
    def get_latest_price_by_date_of_stock(stock_code):
        try:
        #    we don't have price in staturday and sunday, if today is weeken --> price should be friday's price
            stock = Vnstock().stock(symbol=stock_code, source='VCI')
            today = datetime.now()
            if today.weekday() == 5:  # Saturday
                start_date = (today - timedelta(days=1)).strftime("%Y-%m-%d")
            elif today.weekday() == 6:  # Sunday
                start_date = (today - timedelta(days=2)).strftime("%Y-%m-%d")
            else:
                start_date = today.strftime("%Y-%m-%d")
            
            df = stock.quote.history(
                start=start_date,
                end=(today + timedelta(days=1)).strftime("%Y-%m-%d"),
                interval='1D'
            )

            if df.empty:
                print("No data found for the given date range.")
                return None
    
            latest_price = df.tail(1)['close'].values[0]
            return latest_price
        except Exception as e:
            print(f"Error fetching stock price: {e}")
            return None
        
    @staticmethod
    def get_current_price_in_real_time(stock_code):
        try:
            stock = Vnstock().stock(symbol=stock_code, source='VCI')
            # interval '1m' for 1 minute data
            today = datetime.now()

            df = stock.quote.history(
                start=today.strftime("%Y-%m-%d"),
                end=today.strftime("%Y-%m-%d"),
                interval='1m'
            )

            return df.tail(1)['close'].values[0]
        except Exception as e:
            print(f"Error fetching real-time stock price: {e}")
            return None

    @staticmethod
    def get_price_between_time(stock_code, start_date, end_date):
        try:
            stock = Vnstock().stock(symbol=stock_code, source='VCI')
            df = stock.quote.history(
                start=start_date,
                end=end_date,
                interval='1m'
            )
            if df.empty:
                print("No data found for the given date range.")
                return None
            return df
        except Exception as e:
            print(f"Error fetching stock prices between dates: {e}")
            return None
        
    @staticmethod
    def quote_intraday(stock_code):
        try:
            stock = Vnstock().stock(symbol=stock_code, source='VCI')
            df = stock.quote.intraday(page_size = 10_000)
            if df.empty:
                print("No intraday data found.")
                return None
            return df
        except Exception as e:
            print(f"Error fetching intraday stock data: {e}")
            return None    