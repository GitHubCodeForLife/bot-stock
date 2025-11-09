from pandas import DataFrame
from vnstock import Quote

stock_code = 'VIX'
quote = Quote(symbol=stock_code, source='VCI')
intraday : DataFrame = quote.intraday(page_size = 10_000)

# sum volumee of all match_type = Sell and volume >= 10000
print("Sell: ")
print( intraday[(intraday['match_type'] == 'Sell') & (intraday['volume'] >= 10000)]['volume'].sum())

# sum volumee of all match_type = Buy and volume >= 10000
print("Buy: ")
print(intraday[(intraday['match_type'] == 'Buy') & (intraday['volume'] >= 10000)]['volume'].sum())
