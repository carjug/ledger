import unittest

from os import path
from ledger.bank_statement import BankStatement


class TestBankStatement(unittest.TestCase):
    TestDataPath = path.join(path.dirname(path.abspath(__file__)), './test_data/test_data.csv')

    def setUp(self):
        self.bank_statement = BankStatement(self.TestDataPath)

    def test_bank_statement_account_names(self):
        """Test BankStatement.account_names property returns full list of account names"""

        expected = ['alice', 'bob', 'charlie', 'chip', 'dale', 'insurance',
                    'john', 'mary', 'pharmacy', 'samantha', 'supermarket']
        self.assertEqual(expected, self.bank_statement.account_names)

    def test_bank_statement_date_range(self):
        """Test BankStatement.date_range property returns tuple of the earliest and latest dates in the data set"""

        self.assertEqual(('2015-01-01', '2015-01-24'), self.bank_statement.date_range)

    def test_calculate_balance(self):
        """Test BankStatement.balance_calculation() for account name: 'john'"""
        balance = self.bank_statement.calculate_balance('2015-02-01', 'john')
        self.assertEqual(-115.00, balance)

    def test_calculate_balance_for_unknown_account_name(self):
        """Test BankStatement.balance_calculation() for an account name that is not included in the data set"""

        balance = self.bank_statement.calculate_balance('2015-02-01', 'marie')
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_early_date(self):
        """Test BankStatement.balance_calculation() for a date earlier than the earliest date in our data set"""

        balance = self.bank_statement.calculate_balance('1989-01-01', 'john')
        self.assertEqual(0.00, balance)

    def test_calculate_balance_for_null_account_name(self):
        """Test BankStatement.balance_inquiry() when account name is None"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, '2017-01-01', None)

    def test_calculate_balance_for_null_date(self):
        """Test BankStatement.balance_inquiry() when date is None"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, None, 'john')

    def test_balance_inquiry(self):
        """Test BankStatement().balance_inquiry() for account name: 'mary', date: '2017-01-15'"""
        results = self.bank_statement.balance_inquiry('2017-01-15', 'mary')
        self.assertEqual(results, "The balance for mary's account on 2017-01-15 is 25.00")
