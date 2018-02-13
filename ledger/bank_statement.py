from datetime import datetime

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
        # assert account_name is in our data set
        self.validate_account_name_exists(account_name)

        # assert date exists and is properly formatted
        self.validate_date(date)

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

    def _get_account_names(self):
        """
        Creates a set() of all account names in self.data

        :returns: a sorted list
        """
        account_names = set()

        for index, row in self.data.iterrows():
            account_names.add(row['to_account'])
            account_names.add(row['from_account'])

        # sort set alphabetically and return
        return sorted(account_names)

    def _get_date_range(self):
        """
        Creates a set() of all dates in self.data and calculates the earliest and the latest dates

        :returns: a tuple of the earliest and latest dates
        """
        dates = set()

        for index, row in self.data.iterrows():
            dates.add(row['date'])

        earliest_date = min(dates)
        latest_date = max(dates)

        return earliest_date, latest_date

    def validate_account_name_exists(self, account_name):
        """
        :param account_name: the account name to validate
        :type account_name: str

        :returns: raises if invalid or None
        """
        if not account_name:
            raise ValueError("account_name must be supplied to perform a balance inquiry")

        if account_name not in self.account_names:
            raise ValueError("Account: {} does not exist in the data set".format(account_name))

    @property
    def account_names(self):
        return self._get_account_names()

    @property
    def date_range(self):
        return self._get_date_range()

    @staticmethod
    def validate_date(date):
        """
        :param date: the date to validate
        :type date: str

        :returns: raises if invalid or None
        """
        if not date:
            raise ValueError("date must be supplied to perform a balance inquiry")

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")




