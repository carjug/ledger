import unittest

from ledger.bank_statement import BankStatement


class TestBankStatement(unittest.TestCase):

    def test_load_csv(self):
        results = BankStatement.load_data('./test_data.csv')
        self.assertIsNotNone(results)

    def test_load_csv_dataframe_values(self):
        expected_columns = ['date', 'from_account', 'to_account', 'amount']
        dataframe = BankStatement.load_data('./test_data.csv')
        actual_columns = list(dataframe)

        self.assertEqual(expected_columns, actual_columns)
