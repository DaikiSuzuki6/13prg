"""
BankClasses program. Simulates a bank/customers/accounts/transactions/dates

Daiki Suzuki
Total= -66
"""
import doctest


class MyDate:
    """
    A date object to represent a date
    """
    def __init__(self, day, month, year):
        self.day = day  # -1
        self.month = month  # -1
        self.year = year

    def __str__(self):  # -1
        return f"{self.day}/{self.month}/{self.year}"


class Transaction:
    """
    Represents a single transaction. It's called with a transaction type of
    either a deposit or a withdrawal.
    If there are insufficient funds to complete the withdrawal, the
    transaction_type is set to no transaction.
    """
    TRANSACTION_DESCRIPTIONS = ["Deposit", "Withdrawal", "No transaction"]
    DEPOSIT = 0
    WITHDRAWAL = 1
    NO_TRANSACTION = 2

    def __init__(self, amount, transaction_type, date, current_balance):  # -1
        self.amount = amount
        self.transaction_type = transaction_type
        if transaction_type == self.DEPOSIT:
            self.transaction_type = self.TRANSACTION_DESCRIPTIONS[0]
            self._balance_after_transaction = amount + current_balance
        elif transaction_type == self.WITHDRAWAL:
            if current_balance - amount < 0:
                self.transaction_type = self.TRANSACTION_DESCRIPTIONS[2]
                self._balance_after_transaction = current_balance
            else:
                self.transaction_type = self.TRANSACTION_DESCRIPTIONS[1]
                self._balance_after_transaction = current_balance - amount

        self.date = date
        self.current_balance = current_balance  # -1

    def get_type_index(self):  # 0 = deposit, 1 = withdrawal, 2=no transaction
        return self.transaction_type  # -1

    def get_amount(self):
        return self.amount

    def get_balance_after_transaction(self):
        return self._balance_after_transaction

    def __str__(self):  # e.g. 24/1/2021 Deposit $500 Balance: $11700 or
        if self.transaction_type == self.TRANSACTION_DESCRIPTIONS[2]:
            return f"{self.date} {self.transaction_type} Balance: ${self._balance_after_transaction}"
        else:
            return f"{self.date} {self.transaction_type} ${self.amount} Balance: ${self._balance_after_transaction}"
# -1


class Account:
    """
    A bank account. Contains a list of transactions.
    """
    ACCOUNT_TYPE = "GET RICH QUICK ACCOUNT"

    def __init__(self, id):
        self.id = id
        self.account_id = f"{self.ACCOUNT_TYPE} ACCOUNT [{id}]"
        self.is_open = True
        self.transactions = []
        self.balance = 0  # -1

    def get_is_open(self):
        return self.is_open

    def get_current_balance(self):
        return self.balance

    def set_is_open(self, set_open):
        self.is_open = False  # -1

    def close_account(self, date):
        if self.balance > 0:
            Transaction(current_balance=0)  # -3
        self.is_open = False
        return date

    def perform_transaction(self, amount, transaction_type, date):
        transaction = Transaction(amount, transaction_type, date, self.balance)
        self.balance = transaction.get_balance_after_transaction()
        if transaction_type == Transaction.WITHDRAWAL:
            if self.balance - amount < 0:
                self.is_open = False
                return self.is_open
            elif self.balance - amount >= 0:
                self.is_open = True
                return self.is_open
        if transaction_type == Transaction.DEPOSIT:
            self.is_open = True
            return self.is_open
        else:
            self.transactions.append(transaction)
            return self.get_is_open()  # -2

    def get_max_10_transactions(self):
        return "\n".join([f"{i+1} {item}" for i, item in enumerate(self.transactions[-10:])])

    def __str__(self):
        pass  # -3



class Customer:
    """
    Represents a customer of a bank. They only have 1 account.
    """
    def __init__(self, person_name, person_id, account_id):
        self.person_name = person_name  # -1
        self.person_id = person_id
        self.account_id = account_id

    def get_customer_id(self):
        return self.get_customer_id()  # -1

    def get_name(self):
        return self.person_name

    def get_account_balance(self):
        return self.account.get_current_balance()

    def has_an_open_account(self):
        return self.account.get_is_open()

    def close_account(self, date):
        return self.account.close_account()

    def open_account(self, date):
        pass  # -1

    def perform_transaction(self, amount, transaction_type, date):
        pass  # -1

    def get_max_10_transactions(self):
        pass  # -1

    def get_account_information(self):
        pass  # -1

    def __str__(self):
        pass  # -1


class MyBank:
    """
    Represents a bank. Contains customers.
    """
    def __init__(self, name):
        pass  # -4

    def get_mydate_object(self):
        pass  # -2

    def deposit_funds(self, current_customer):
        pass  # -1

    def withdraw_funds(self, current_customer):
        pass  # -1

    def open_account(self, current_customer):
        pass  # -1

    def close_account(self, current_customer):
        pass  # -1

    def display_bank_summary(self):
        pass  # -5

    def display_account_information(self, customer):
        pass  # -1

    def display_welcome(self):
        pass  # -2

    def add_customer(self, customer):
        pass  # -1

    def remove_customer(self, customer):
        pass  # -1
# -22 tests failed.


def test_bank():
    """
    # Mydate , Transaction , Account testing
    # ==== #
    # MyDate Class
    >>> date1 = MyDate(3, 12, 2021)
    >>> print(date1)
    3/12/2021

    >>> date2 = MyDate(23, 4, 2021)
    >>> print(date2)
    23/4/2021

    # ==== #
    # Transaction Class
    print("Preliminary testing of the Transaction class")
    >>> transaction = Transaction(100, Transaction.DEPOSIT, MyDate(3, 1, 2021),
    ... 3000)
    >>> print(transaction)
    3/1/2021 Deposit $100 Balance: $3100

    >>> transaction2 = Transaction(300, Transaction.WITHDRAWAL, MyDate(3, 1,
    ... 2021), 600)
    >>> print(transaction2)
    3/1/2021 Withdrawal $300 Balance: $300

    >>> transaction3 = Transaction(100.01, Transaction.WITHDRAWAL, MyDate(3, 1,
    ... 2021), 100)
    >>> print(transaction3)
    3/1/2021 No transaction Balance: $100

    # ==== #
    # Account Class
    print("Preliminary testing of the Account class")

    # -- 1 -- #
    >>> account = Account(1234)
    >>> account.perform_transaction(200, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> print('1. Balance $' + str(account.get_current_balance()))
    1. Balance $200
    >>> account.perform_transaction(600, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $800

    # -- 2 -- #
    >>> account = Account(1234)

    # Transactions
    >>> account.perform_transaction(200, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(100, Transaction.WITHDRAWAL, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(100.01, Transaction.WITHDRAWAL, MyDate(23,
    ... 4, 2021))
    False
    >>> account.perform_transaction(700, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(800, Transaction.WITHDRAWAL, MyDate(23, 4,
    ... 2021))
    True
    >>> print(account.get_max_10_transactions())
    1 23/4/2021 Deposit $200 Balance: $200
    2 23/4/2021 Withdrawal $100 Balance: $100
    3 23/4/2021 No transaction Balance: $100
    4 23/4/2021 Deposit $700 Balance: $800
    5 23/4/2021 Withdrawal $800 Balance: $0
    <BLANKLINE>

    # -- 3 -- #
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $0

    # -- 4 -- #
    >>> account.close_account(MyDate(1, 1, 9999))
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $0 Account closed

    # -- 5 -- #
    >>> account = Account(1234)
    >>> deposits = [35, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    >>> for deposit in deposits:
    ...     account.perform_transaction(deposit, Transaction.DEPOSIT,
    ... MyDate(25, 4, 2021))
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    >>> print(account.get_max_10_transactions())
    1 25/4/2021 Deposit $25 Balance: $60
    2 25/4/2021 Deposit $30 Balance: $90
    3 25/4/2021 Deposit $35 Balance: $125
    4 25/4/2021 Deposit $40 Balance: $165
    5 25/4/2021 Deposit $45 Balance: $210
    6 25/4/2021 Deposit $50 Balance: $260
    7 25/4/2021 Deposit $55 Balance: $315
    8 25/4/2021 Deposit $60 Balance: $375
    9 25/4/2021 Deposit $65 Balance: $440
    10 25/4/2021 Deposit $70 Balance: $510
    <BLANKLINE>

    # Customer class

    >>> cust = Customer("Mr. Gardiner", 1, 1000)
    >>> print(cust)
    Name: Mr. Gardiner
    Customer ID: 1
    GET_RICH_QUICK ACCOUNT [1000]: Balance $0
    >>> cust.perform_transaction(1000, Transaction.DEPOSIT, MyDate(27, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(300, Transaction.WITHDRAWAL, MyDate(27, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(250, Transaction.WITHDRAWAL, MyDate(28, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(500, Transaction.WITHDRAWAL, MyDate(1, 3,
    ... 2022))
    False
    >>> print(cust.get_max_10_transactions())
    1 27/2/2022 Deposit $1000 Balance: $1000
    2 27/2/2022 Withdrawal $300 Balance: $700
    3 28/2/2022 Withdrawal $250 Balance: $450
    4 1/3/2022 No transaction Balance: $450
    <BLANKLINE>
    >>> cust.close_account(MyDate(2, 3, 2022))
    >>> print(cust)
    Name: Mr. Gardiner
    Customer ID: 1
    GET_RICH_QUICK ACCOUNT [1000]: Balance $0 Account closed
    >>> cust.open_account(MyDate(3, 3, 2022))
    >>> print(cust.get_max_10_transactions())
    1 27/2/2022 Deposit $1000 Balance: $1000
    2 27/2/2022 Withdrawal $300 Balance: $700
    3 28/2/2022 Withdrawal $250 Balance: $450
    4 1/3/2022 No transaction Balance: $450
    5 2/3/2022 Withdrawal $450 Balance: $0
    6 3/3/2022 Deposit $0 Balance: $0
    <BLANKLINE>

    # MyBank class
    >>> take_my_money = MyBank("TakeMyMoney")
    >>> customers = []
    >>> customers.append(Customer("Mr. Gardiner", 1, 1001))
    >>> customers.append(Customer("Mr. Bean", 2, 1002))
    >>> customers.append(Customer("Gabe Newell", 3, 1003))
    >>> customers.append(Customer("Winnie the Pooh", 4, 1004))
    >>> for customer in customers:
    ...     take_my_money.add_customer(customer)
    >>> take_my_money.close_account(customers[1])
    GET_RICH_QUICK ACCOUNT [1002]: Balance $0 Account closed
    >>> import io, sys
    >>> sys.stdin = io.StringIO("500.5")  # input
    >>> take_my_money.deposit_funds(customers[0])
    Enter the amount to deposit:
    >>> take_my_money.deposit_funds(customers[1])   # Should fail
    ...                                             # Account is closed
    Account is closed!
    >>> sys.stdin = io.StringIO("600")  # input
    >>> take_my_money.deposit_funds(customers[3])   # Enter 600
    Enter the amount to deposit:
    >>> sys.stdin = io.StringIO("200")  # input
    >>> take_my_money.withdraw_funds(customers[0]) # Enter 200
    Enter the amount to withdraw:
    >>> take_my_money.display_bank_summary()
    <BLANKLINE>
    ************************************************************************
    TakeMyMoney has 3 customers
    Total amount in customer accounts $900.5
    ************************************************************************
    <BLANKLINE>
    """
    pass


doctest.testmod()  # or doctest.testmod(verbose=True)