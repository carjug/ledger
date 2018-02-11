import unittest

from ledger.bank_statement import BankStatement
from utils.csv_utils import CSVLoader


class TestBankStatement(unittest.TestCase):
    TestDataDir = './test_data/test_data.csv'

    def test_calculate_balance(self):
        """Test balance calculation for account name: 'john'"""

        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('2015-02-01', 'john', df)
        self.assertEqual(-115.00, balance)

    def test_calculate_balance_for_unknown_account_name(self):
        """Test balance calculation for an account name that is not included in the data set"""

        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('2015-02-01', 'marie', df)
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_early_date(self):
        """Test balance calculation for a date earlier than the earliest date in our data set"""

        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('1989-01-01', 'john', df)
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_null_account_name(self):
        """Test balance calculation when account name is None"""

        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        self.assertRaises(ValueError, BankStatement.calculate_balance, '2017-01-01', None, df)

    def test_calculate_balance_for_null_date(self):
        """Test balance calculation when date is None"""

        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        self.assertRaises(ValueError, BankStatement.calculate_balance, None, 'john', df)
