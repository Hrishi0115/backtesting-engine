# Contains the abstract class for data loaders and concrete implementations like `YahooFinanceLoader`

from abc import ABC, abstractmethod
import pandas as pd
import yfinance as yf

class DataLoader(ABC):
    @abstractmethod
    def load_data(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass

class YahooFinanceLoader(DataLoader):
    def load_data(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        data.reset_index(inplace=True)
        return data