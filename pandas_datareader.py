import akshare as ak
import pandas as pd

class data:
    @classmethod
    def __DataReader(cls,symbol, source, start_date, end_date):
        if source == 'sina': 
            data = ak.stock_us_daily(symbol=symbol, adjust="")
            data.rename(columns={
                'date': 'Date',
                'open': 'Open',
                'close': 'Close',
                'low': 'Low',
                'high': 'High',
                'volume': 'Volume'
                }, inplace=True)
            data.set_index('Date', inplace=True)
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
            data["Adj Close"] = data["Close"]
            return data.loc[start_date:end_date]
        elif source == 'eastmoney':
            data = ak.stock_us_hist(symbol=symbol, period="daily", start_date=start_date.replace('-', ''), end_date=end_date.replace('-', ''), adjust="hfq")
            data.rename(columns={
                '日期': 'Date',
                '开盘': 'Open',
                '收盘': 'Close',
                '最低': 'Low',
                '最高': 'High',
                '成交量': 'Volume'
                }, inplace=True)
            data.set_index('Date', inplace=True)
            data["Adj Close"] = data["Close"]
            return data
        elif source == 'yahoo':
            import yfinance as yf
            import os
            proxy = 'http://127.0.0.1:10808' # 代理设置，此处修改
            os.environ['HTTP_PROXY'] = proxy 
            os.environ['HTTPS_PROXY'] = proxy 
            data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=True, back_adjust=True)
            data.columns = data.columns.get_level_values(0)
            data["Adj Close"] = data["Close"]
            return data
        else:
            raise ValueError(f"Unknown source: {source}")

    @classmethod
    def  DataReader(cls, symbols, source, start_date, end_date):
        if isinstance(symbols, str):
            return cls.__DataReader(symbols, source, start_date, end_date)
        else:
            frames = dict()
            for symbol in symbols:
                frames[symbol] = cls.__DataReader(symbol, source, start_date, end_date)
            return pd.concat(frames.values(), axis=1, keys=symbols)

        