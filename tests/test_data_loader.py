# What is unit testing?

# Unit testing involves for individual units of code (e.g., functions or methods) to ensure they work as expected. The `unitest` module in Python is a built-in framework
# for writing and running tests.

# Components of a Unit Test

# 1. Test Framework: `unitest` is the framework we're using to write and run our tests
# 2. Test Case: A class that inherits from `unitest.TestCase`. This class contains one or more test methods
# 3. Test Method: A method within the test case class that tests a specific aspect of the code
# 4. Assertions: Statements that check if certain conditions are true. If an assertion fails, the test fails

# Example workflow

import unittest
from app.data_loader import load_historical_data

class TestDataLoader(unittest.TestCase):
    # groups related tests for the `load_historical_data` function
    def test_load_historical_data(self):
        symbol = "AAPL"
        start_date = "2021-01-01"
        end_date = "2021-12-31"

        data = load_historical_data(symbol,start_date,end_date)
        self.assertIsNotNone(data, "Data should not be None") # some instances where data should be none however, for example if the function
        # is called during a weekend, public holiday, etc. - so maybe this test case could be made more robust - by checking if it empty only when it shouldn't be
        self.assertIsInstance(data, list, "Data should be a list")
        self.assertGreater(len(data), 0, "Data list should not be empty") # again - there are possible instances where the data list should be empty so can make this test case
        # more robust too
        # print("Data fetched successfully!")
        # print(data[:5]) # print the first 5 records for verification

if __name__ == "__main__":
    unittest.main()

