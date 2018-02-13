import unittest
import pandas

from os import path

from file_loaders.csv_loader import CSVLoader


class TestCSVLoader(unittest.TestCase):
    TestDataPath = path.join(path.dirname(path.abspath(__file__)), './test_data/test_data.csv')

    def test_load_as_dataframe(self):
        """Test that CSVLoader.load_as_dataframe returns a pandas.DataFrame"""

        results = CSVLoader.load_as_dataframe(self.TestDataPath)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, pandas.DataFrame)

    def test_load_as_dataframe_values(self):
        """Test that CSVLoader.load_as_dataframe returns a dataframe with the correct column names"""

        expected_columns = ['date', 'from_account', 'to_account', 'amount']
        dataframe = CSVLoader.load_as_dataframe(self.TestDataPath)
        actual_columns = list(dataframe)

        self.assertEqual(expected_columns, actual_columns)

    def test_load_as_dataframe_bad_file_path(self):
        """Test that CSVLoader.load_as_dataframe raises an IOError when the file cannot be found"""

        # assert that an IOError is raised if the .csv file cannot be found
        self.assertRaises(IOError, CSVLoader.load_as_dataframe, 'non_existent_test_file.csv')

    def test_validate_file_path_bad_file_path(self):
        """Test CSVLoader.validate_file_path raises when invalid"""

        # assert a ValueError if the file_path is None
        self.assertRaises(ValueError, CSVLoader.validate_file_path, None)

        # assert a ValueError if the file_path does not point to a .csv file
        self.assertRaises(ValueError, CSVLoader.validate_file_path, 'non_existent_test_file.txt')
