import unittest

import pandas

from file_loaders.csv_loader import CSVLoader
from test_bank_statement import TestBankStatement as tbs


class TestCSVLoader(unittest.TestCase):

    def test_load_as_dataframe(self):
        """Test that CSVLoader.load_as_dataframe returns a pandas.DataFrame"""

        results = CSVLoader.load_as_dataframe(tbs.TestDataPath)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, pandas.DataFrame)

    def test_load_as_dataframe_values(self):
        """Test that CSVLoader.load_as_dataframe returns a dataframe with the correct column names"""

        expected_columns = ['date', 'from_account', 'to_account', 'amount']
        dataframe = CSVLoader.load_as_dataframe(tbs.TestDataPath)
        actual_columns = list(dataframe)

        self.assertEqual(expected_columns, actual_columns)

    def test_load_as_dataframe_bad_file_path(self):
        """Test CSVLoader.load_as_dataframe raises with bad input"""

        # assert that an IOError is raised if the .csv file cannot be found
        self.assertRaises(IOError, CSVLoader.load_as_dataframe, 'non_existent_test_file.csv')

        # assert a ValueError if the file_path is None
        self.assertRaises(ValueError, CSVLoader.load_as_dataframe, None)

        # assert a ValueError if the file_path does not point to a .csv file
        self.assertRaises(ValueError, CSVLoader.load_as_dataframe, 'non_existent_test_file.txt')
