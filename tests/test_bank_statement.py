import unittest

from ledger.bank_statement import BankStatement
from file_loaders.csv_loader import CSVLoader


class TestBankStatement(unittest.TestCase):
    TestDataPath = './test_data/test_data.csv'

    def test_calculate_balance(self):
        """Test BankStatement.balance_calculation() for account name: 'john'"""

        df = CSVLoader.load_as_dataframe(self.TestDataPath)
        balance = BankStatement.calculate_balance('2015-02-01', 'john', df)
        self.assertEqual(-115.00, balance)

    def test_calculate_balance_for_unknown_account_name(self):
        """Test BankStatement.balance_calculation() for an account name that is not included in the data set"""

        df = CSVLoader.load_as_dataframe(self.TestDataPath)
        balance = BankStatement.calculate_balance('2015-02-01', 'marie', df)
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_early_date(self):
        """Test BankStatement.balance_calculation() for a date earlier than the earliest date in our data set"""

        df = CSVLoader.load_as_dataframe(self.TestDataPath)
        balance = BankStatement.calculate_balance('1989-01-01', 'john', df)
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_null_account_name(self):
        """Test BankStatement.balance_calculation() when account name is None"""

        df = CSVLoader.load_as_dataframe(self.TestDataPath)
        self.assertRaises(ValueError, BankStatement.calculate_balance, '2017-01-01', None, df)

    def test_calculate_balance_for_null_date(self):
        """Test BankStatement.balance_calculation() when date is None"""

        df = CSVLoader.load_as_dataframe(self.TestDataPath)
        self.assertRaises(ValueError, BankStatement.calculate_balance, None, 'john', df)

    def test_balance_inquiry(self):
        """Test BankStatement().balance_inquiry() for account name: 'mary', date: '2017-01-15'"""
        results = BankStatement().balance_inquiry('2017-01-15', 'mary', self.TestDataPath)
        self.assertEqual(results, "The balance for mary's account on 2017-01-15 is 25.00")
