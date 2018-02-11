from file_loaders.csv_loader import CSVLoader


class BankStatement(object):
    """
    BankStatement is a class used to retrieve balance information for an account.
    The BankStatement class needs to be initialized with a .csv seed data file
    containing the following columns: date,from_account,to_account,amount.
    Note: the required date format is `YYYY-MM-DD`.
    """

    def __init__(self, file_path):
        """
        Initialize BankStatement class with .csv data

        :param file_path: a path to a .csv file containing all cross-account transactional data
        :type file_path: str
        """

        self.data = CSVLoader.load_as_dataframe(file_path)

    def balance_inquiry(self, date, account_name):
        """
        Loads csv data, calculates the balance, and returns a formatted string containing the account information

        :param date: the date on which to calculate the account balance
        :type date: str
        :param account_name: the account name for whom to calculate the balance
        :type account_name: str

        :returns: a formatted string
        """

        account_value = self.calculate_balance(date, account_name)

        return "The balance for {}'s account on {} is {}".format(account_name, date, format(account_value, '.2f'))

    def calculate_balance(self, date, account_name):
        """
        Calculates and returns the balance for the account on the date supplied

        :param date: the date on which to calculate the account balance
        :type date: str
        :param account_name: the account name for whom to calculate the balance
        :type account_name: str

        :returns: a float of the balance
        """

        if not account_name:
            raise ValueError("account_name must be supplied to perform a balance inquiry")

        if not date:
            raise ValueError("date must be supplied to perform a balance inquiry")

        # initialize all accounts at 0.00 per the exercise specifications
        account_value = 0.00

        for index, row in self.data.iterrows():
            # only calculate rows for which the date is earlier or equal to the date specified by the user
            if row['date'] <= date:
                if row['from_account'] == account_name:
                    # debit the account
                    account_value -= row['amount']

                if row['to_account'] == account_name:
                    # credit the account
                    account_value += row['amount']
        return account_value
