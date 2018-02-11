import unittest

from file_loaders.csv_loader import CSVLoader
from test_bank_statement import TestBankStatement as tbs


class TestCSVLoader(unittest.TestCase):

    def test_load_as_dataframe(self):
        """"""
        results = CSVLoader.load_as_dataframe(tbs.TestDataPath)
        self.assertIsNotNone(results)

    def test_load_as_dataframe_values(self):
        """"""
        expected_columns = ['date', 'from_account', 'to_account', 'amount']
        dataframe = CSVLoader.load_as_dataframe(tbs.TestDataPath)
        actual_columns = list(dataframe)

        self.assertEqual(expected_columns, actual_columns)

    def test_load_as_dataframe_bad_file_path(self):
        """"""
        # assert that an IOError is raised if the .csv file cannot be found
        self.assertRaises(IOError, CSVLoader.load_as_dataframe, 'non_existent_test_file.csv')

        # assert a ValueError if the file_path is not supplied
        self.assertRaises(ValueError, CSVLoader.load_as_dataframe, None)

        # assert a ValueError if the file_path does not point to a .csv file
        self.assertRaises(ValueError, CSVLoader.load_as_dataframe, 'non_existent_test_file.txt')
