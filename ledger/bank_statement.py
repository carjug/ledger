#!/usr/bin/env python
#  -*- coding: utf-8 -*-


class BankStatement(object):

    def balance_inquiry(self, date, account_name, file_path):
        data = self.load_data(file_path)
        account_value = self.calculate_balance(account_name, data, date)

        return "The balance for {}'s account is {}".format(account_name, format(account_value, '.2f'))

    @classmethod
    def calculate_balance(cls, account_name, data, date):
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
    def load_data(cls, file_path):
        with open(file_path, 'rb') as fp:
            data = list(csv.DictReader(fp))
        return data


if __name__ == 'main':
    pass