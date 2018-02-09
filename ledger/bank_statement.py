#!/usr/bin/env python
#  -*- coding: utf-8 -*-


class BankStatement(object):

    def balance_inquiry(self, date, account_name, file_path):
        data = self.load_data(file_path)
        return data

    @classmethod
    def load_data(cls, file_path):
        with open(file_path, 'rb') as fp:
            data = list(csv.DictReader(fp))
        return data


if __name__ == 'main':
    pass