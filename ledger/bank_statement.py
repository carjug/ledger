from utils.csv_utils import CSVLoader


class BankStatement(object):

    def balance_inquiry(self, date, account_name, file_path):
        """Loads csv data, calculates the balance, and returns a formatted string containing the account information"""

        data = CSVLoader.load_as_dataframe(file_path)
        account_value = self.calculate_balance(account_name, data, date)

        return "The balance for {}'s account on {} is {}".format(account_name, date, format(account_value, '.2f'))

    @classmethod
    def calculate_balance(cls, account_name, data, date):
        # initialize all accounts at 0.00 per the exercise specifications
        account_value = 0.00

        for index, row in data.iterrows():
            if row['date'] <= date:
                if row['from_account'] == account_name:
                    # debit the account
                    account_value -= row['amount']

                if row['to_account'] == account_name:
                    # credit the account
                    account_value += row['amount']
        return account_value
