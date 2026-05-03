import yfinance as yf
import os
proxy = 'http://127.0.0.1:10808' # 代理设置，此处修改
os.environ['HTTP_PROXY'] = proxy 
os.environ['HTTPS_PROXY'] = proxy 

train_data =  yf.download("GOOG", start="2014-01-01", end="2018-01-01", auto_adjust=False)
print(train_data.head())
print("OK")