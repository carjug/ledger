from utils.csv_utils import CSVLoader


class BankStatement(object):

    def balance_inquiry(self, date, account_name, file_path):
        data = self.load_csv_as_dataframe(file_path)
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

    @classmethod
    def load_csv_as_dataframe(cls, file_path):
        if not file_path:
            raise ValueError("A path to a .csv file must be supplied.")
        try:
            import pandas as pd
            dataframe = pd.read_csv(file_path)
        except IOError as e:
            raise IOError("Failed to load {}, with message: {}".format(file_path, e.message))

        return dataframe


if __name__ == 'main':
    pass
