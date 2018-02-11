import unittest

from ledger.bank_statement import BankStatement
from utils.csv_utils import CSVLoader


class TestBankStatement(unittest.TestCase):
    TestDataDir = './test_data/test_data.csv'

    def test_calculate_balance(self):
        """"""
        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('john', df, '2015-02-01')
        self.assertEqual(-115.00, balance)

    def test_calculate_balance_for_unknown_account_name(self):
        """"""
        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('marie', df, '2015-02-01')
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_early_date(self):
        """"""
        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        balance = BankStatement.calculate_balance('john', df, '1989-01-01')
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_null_account_name(self):
        """"""
        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        self.assertRaises(ValueError, BankStatement.calculate_balance, None, df, '2017-01-01')

    def test_calculate_balance_for_null_date(self):
        """"""
        df = CSVLoader.load_as_dataframe(self.TestDataDir)
        self.assertRaises(ValueError, BankStatement.calculate_balance, 'john', df, None)
