# Contains the logic to load historical market data

import pandas as pd
import yfinance as yf

# historical data provider: yahoo finance 

def load_historical_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol)
    data = ticker.history(start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data.to_dict(orient='records')
