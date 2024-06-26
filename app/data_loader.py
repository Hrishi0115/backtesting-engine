# Contains the logic to load historical market data

import pandas as pd
import yfinance as yf

# historical data provider: yahoo finance 

def load_historical_data(symbol, start_date, end_date):
    """
    Fetches historical market data for a given symbol and date range from Yahoo Finance.

    Args:
    - symbol (str): The ticker symbol of the stock (e.g., "AAPL).
    - start_date (str): The start date in "YYYY-MM-DD" format.
    - end_date (str): The end date in "YYYY-MM-DD" format.
    
    Returns:
    - List[dict]: A list of dictionaries containing the historical data.
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        data.reset_index(inplace=True)
        # consider formatting date column, i.e. data['Date'] = pd.to_datetime(data['Date]).dt.strftime('%Y-%m-%d')
        print(f"Data fetched successfully")
        return data.to_dict(orient='records')
    
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return None
