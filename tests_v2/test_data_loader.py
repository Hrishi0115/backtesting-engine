import unittest
import pandas as pd
from app_v2.data_loader import YahooFinanceLoader

# The test class `TestYahooFinanceLoader` is inheriting from `unitest.TestCase` - the base class provided by the `unitest` module.

class TestYahooFinanceLoader(unittest.TestCase):
    def setUp(self):
        self.loader = YahooFinanceLoader()
        self.symbol = "AAPL"
        self.start_date = "2021-01-01"
        self.end_date = "2021-12-31"

    def test_load_data(self):
        data = self.loader(self.symbol, self.start_date, self.end_date)
        self.assertIsInstance(data, pd.DataFrame, "Loaded data should be a DataFrame")
        self.assertFalse(data.empty, "Loaded data should not be empty") # TODO: again same issues with the v1 test for the data loader
        self.assertIn('Date', data.columns, "DataFrame should have a 'Date' column")
        self.assertIn('Close', data.columns, "DataFrame should have a 'Close' column")

    # add other tests below like the following:

    def test_load_data_invalid_symbol(self):
        invalid_symbol = "INVALID"
        data = self.loader.load_data(invalid_symbol, self.start_date, self.end_date)
        self.assertIsInstance(data, pd.DataFrame, "Loaded data should be a DataFrame")
        self.assertTrue(data.empty, "Loaded data for an invalid symbol should be empty")

    def test_load_data_date_range(self):
        # Check if the date range is respected
        data = self.loader.load_data(self.symbol, self.start_date, self.end_date)
        self.assertGreaterEqual(data['Date'].min(), pd.to_datetime(self.start_date), "Data start date should be greater than or equal to start_date")
        self.assertLessEqual(data['Date'].max(), pd.to_datetime(self.end_date), "Data end date should be less than or equal to end_date")


if __name__ == "__main__":
    unittest.main()