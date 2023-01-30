from uuid import uuid4
from bank_account import *


class User:
    def __init__(self, fname, lname, nat_code, date_of_birth, password):
        self.fname = fname
        self.lname = lname
        self.__nat_code = nat_code
        self.date_of_birth = date_of_birth
        self.__user_id = uuid4()
        self.__backup_pass = password
        self.bank_account = BankAccount(balance=0)
        self.ticket_list = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def backup_pass(self):
        return self.__backup_pass

    @backup_pass.setter
    def new_pass(self, new_pass):
        self.__backup_pass = new_pass

    def buy_ticket(self, ticket):
        self.ticket_list.append(ticket)

    def use_ticket(self):
        assert self.ticket_list is not None, 'you dont have any ticket'
        return self.ticket_list

    def show_ticket_list(self):
        for tk in self.ticket_list:
            yield tk

    def __repr__(self):
        return f'User: {self.fname} {self.lname}\nUser ID: {self.user_id}' \
               f'\nBank Account ID: {self.bank_account.bank_account_id}'
