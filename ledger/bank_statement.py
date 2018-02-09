#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import csv
# load in csv file
# get balance for a given date and account name


class BankStatement(object):

    def balance_inquiry(self, date, account_name, file_path):
        data = self.load_data(file_path)
        return data

    def load_data(self, file_path):
        with open(file_path, 'rb') as fp:
            data = list(csv.DictReader(fp))
        return data


if __name__ == 'main':
    pass