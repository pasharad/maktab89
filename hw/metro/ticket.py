from uuid import uuid4
from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Ticket(ABC):
    def __init__(self):
        self.creation_date = datetime.now()
        self.ticket_id = uuid4()
        self.cost = 0
        self.balance = 0

    @abstractmethod
    def expire(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ChargeableCard(Ticket):
    def __init__(self):
        super().__init__()
        self.cost = 5

    def expire(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        assert self.balance - amount > 0, 'your charge is not enough, please charge'
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f'Type: Chargeable card\n Card ID: {self.ticket_id}' \
               f'\nCredit: {self.balance}'


class ExpirationCard(Ticket):
    def __init__(self):
        super().__init__()
        self.cost = 55
        self.expire_date = self.creation_date + timedelta(days=365)
        self.balance = 50

    def expire(self):
        return datetime.now()

    def withdraw(self, amount):
        assert self.balance - amount > 0, 'your card has been expired'
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f'Type: Expiration card\nCard ID: {self.ticket_id}' \
               f'\nCredit: {self.balance}\nExpire Date: {self.expire_date}'


class DisposableTicket(Ticket):
    def __init__(self):
        super().__init__()
        self.cost = 2
        self.balance = 1

    def expire(self):
        return self.balance

    def withdraw(self):
        assert self.balance - 1 > 0, 'your ticket has been expired'
        self.balance -= 1

    def __repr__(self):
        return f'Type: Disposable card\n Card ID: {self.ticket_id}'

