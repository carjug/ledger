import unittest

from ledger.bank_statement import BankStatement


class TestBankStatement(unittest.TestCase):

    def test_load_csv(self):
        results = BankStatement.load_data('./test_data.csv')
        self.assertTrue(results)
