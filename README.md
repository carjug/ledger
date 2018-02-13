# Ledger Coding Exercise
Processes a cross-account transactional ledger in the format of a .csv
file, and provides access to each of the accounts' balance at a given
date.

*Note that the columns of the .csv file are*
`date,from_account,to_account,amount`

*Also note that the code that loads the csv file expects a header row of
the aforementioned column names*



## System Requirements
Python 2.7

## Installing / Getting started
How to install this project locally:

```shell
git clone https://github.com/carjug/ledger.git
cd ledger/
pip install -r requirements.txt
```

### Running / Interacting with the code
A few things to note before getting started:
- you must initialize `BankStatement` with a path to a `.csv` file
- a sample csv file exists in `ledger/tests/test_data/test_data.csv`
  - _example:_  `BankStatement('./tests/test_data/test_data.csv')`

Below are some examples of how to interact with the project in a REPL (such
as ipython)

```shell
ipython
from ledger.bank_statement import BankStatement
bank_statement = BankStatement('./tests/test_data/test_data.csv')
bank_statement.balance_inquiry('2015-01-30', 'mary')
```


To get a range of the dates contained in the data set:
```shell
ipython
from ledger.bank_statement import BankStatement
bank_statement = BankStatement('./tests/test_data/test_data.csv')
bank_statement.date_range
```


To get a sorted list of the account names contained in the data set:
```shell
ipython
from ledger.bank_statement import BankStatement
bank_statement = BankStatement('./tests/test_data/test_data.csv')
bank_statement.account_names
```


### Running the tests
To run the unittests from the command line
```shell
python -m unittest discover -v

```
