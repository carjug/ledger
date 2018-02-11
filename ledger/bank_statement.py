from utils.csv_utils import CSVLoader


class BankStatement(object):
    """
    TODO: Fill this out
    """

    def balance_inquiry(self, date, account_name, file_path):
        """
        Loads csv data, calculates the balance, and returns a formatted string containing the account information

        :param date: the date on which to calculate the account balance
        :type date: str
        :param account_name: the account name for whom to calculate the balance
        :type account_name: str
        :param file_path: a path to a .csv file containing all cross-account transactional data
        :type file_path: str

        :returns: a formatted string
        """

        data = CSVLoader.load_as_dataframe(file_path)
        account_value = self.calculate_balance(account_name, data, date)

        return "The balance for {}'s account on {} is {}".format(account_name, date, format(account_value, '.2f'))

    @classmethod
    def calculate_balance(cls, date, account_name, data):
        """
        Calculates and returns the balance for the account on the date supplied

        :param date: the date on which to calculate the account balance
        :type date: str
        :param account_name: the account name for whom to calculate the balance
        :type account_name: str
        :param data: all cross-account transactional data
        :type data: pandas.DataFrame

        :returns: a float of the balance
        """

        if not account_name:
            raise ValueError("account_name must be supplied to perform a balance inquiry")

        if not date:
            raise ValueError("date must be supplied to perform a balance inquiry")

        # initialize all accounts at 0.00 per the exercise specifications
        account_value = 0.00

        for index, row in data.iterrows():
            # only calculate rows for which the date is earlier or equal to the date specified by the user
            if row['date'] <= date:
                if row['from_account'] == account_name:
                    # debit the account
                    account_value -= row['amount']

                if row['to_account'] == account_name:
                    # credit the account
                    account_value += row['amount']
        return account_value
