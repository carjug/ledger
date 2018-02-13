import unittest

from os import path
from ledger.bank_statement import BankStatement


class TestBankStatement(unittest.TestCase):
    TestDataPath = path.join(path.dirname(path.abspath(__file__)), './test_data/test_data.csv')

    def setUp(self):
        self.bank_statement = BankStatement(self.TestDataPath)

    def tearDown(self):
        self.bank_statement = None

    def test_bank_statement_account_names(self):
        """Test BankStatement.account_names property returns full list of account names"""

        expected = ['alice', 'bob', 'charlie', 'chip', 'dale', 'insurance', 'john',
                    'mary', 'pharmacy', 'restaurant', 'samantha', 'supermarket']
        self.assertEqual(expected, self.bank_statement.account_names)

    def test_bank_statement_date_range(self):
        """Test BankStatement.date_range property returns tuple of the earliest and latest dates in the data set"""

        self.assertEqual(('2015-01-01', '2015-01-24'), self.bank_statement.date_range)

    def test_calculate_balance(self):
        """Test BankStatement.calculate_balance() for account name: 'john'"""

        balance = self.bank_statement.calculate_balance('2015-02-01', 'john')
        self.assertEqual(-115.00, balance)

    def test_calculate_balance_for_early_date(self):
        """Test BankStatement.calculate_balance() for a date earlier than the earliest date in our data set"""

        balance = self.bank_statement.calculate_balance('1989-01-01', 'john')
        self.assertEqual(0.00, balance)

    def test_balance_inquiry_for_full_date_range(self):
        """Test BankStatement().balance_inquiry() for account name: 'mary', date: '2017-01-15'"""

        results = self.bank_statement.balance_inquiry('2017-01-15', 'mary')
        self.assertEqual(results, "The balance for mary's account on 2017-01-15 is 45.99")

    def test_balance_inquiry_with_date_in_date_range(self):
        """Test BankStatement().balance_inquiry() for account name: 'alice', date: '2015-01-10'"""

        results = self.bank_statement.balance_inquiry('2015-01-15', 'alice')
        self.assertEqual(results, "The balance for alice's account on 2015-01-15 is -1.65")

    def test_balance_inquiry_with_date_on_transaction_date(self):
        """Test BankStatement().balance_inquiry() when input date and transaction date are equal"""

        results = self.bank_statement.balance_inquiry('2015-01-16', 'mary')
        self.assertEqual(results, "The balance for mary's account on 2015-01-16 is 145.99")

    def test_balance_inquiry_for_null_account_name(self):
        """Test BankStatement.balance_inquiry() when account name is None"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, '2017-01-01', None)

    def test_balance_inquiry_for_account_name_not_in_data_set(self):
        """Test BankStatement.balance_inquiry() when account name is not in the data set"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, '2017-01-01', 'mari')

    def test_balance_inquiry_for_null_date(self):
        """Test BankStatement.balance_inquiry() when date is None"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, None, 'john')

    def test_balance_inquiry_for_improper_date_format(self):
        """Test BankStatement.balance_inquiry() when date is improperly formatted"""

        self.assertRaises(ValueError, self.bank_statement.balance_inquiry, '01-03-2015', 'john')

