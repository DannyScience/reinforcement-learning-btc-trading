import pandas as pd
from binance.client import Client
import datetime as dt
from cred import api_key, api_secret


client = Client(api_key, api_secret)
symbol = "BTCUSDT"
interval='1h'
klines = client.get_historical_klines(symbol, interval, "1 Jan,2023")
data = pd.DataFrame(klines)
data.columns = ['time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
#data.index = [dt.datetime.fromtimestamp(x/1000.0) for x in data.close_time]
df= data.astype(float)
df["close"].plot(title = 'BTCUSDT', legend = 'close')
df=df.drop(['close_time','taker_base_vol','taker_quote_vol', 'ignore', 'qav','num_trades'], axis=1)
