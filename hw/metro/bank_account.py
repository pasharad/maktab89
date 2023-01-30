from random import randint


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.bank_account_id = randint(1000000000, 9999999999)
        self.min = 5

    def deposit(self, amount):
        self.balance += amount
        return f'your action was successful\nyour balance is: {self.balance}'

    def withdraw(self, amount):
        assert self.balance - amount >= self.min, 'your balance is not enough!!!'
        self.balance -= amount
        return f'your action was successful\nyour balance is: {self.balance}'

    def show_balance(self, fullname):
        assert self.balance - 1 >= self.min, 'your balance is not enough!!!'
        self.balance -= 1
        return f'User: {fullname}\nBalance: {self.balance}\nNote: reduce 1$ for wage'
