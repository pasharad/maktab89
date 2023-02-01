from user import *
from ticket import *


class Transportation:
    def __init__(self, tr_id, origin, destination, cost):
        self.tr_id = tr_id
        self.origin = origin
        self.destination = destination
        self.cost = cost


class Admin(User):
    def __init__(self, fname, lname, nat_code, date_of_birth, password):
        super().__init__(fname, lname, nat_code, date_of_birth, password)
        self.transport = []

    def make_transport(self, tr_id, origin, destination, cost):
        new_transport = Transportation(tr_id, origin, destination, cost)
        self.transport.append(new_transport)

    @classmethod
    def edit_transport(cls, tr_id, origin, destination, cost):
        cls.tr_id = tr_id
        cls.cost = cost
        cls.origin = origin
        cls.destination = destination

    @staticmethod
    def create_ticket(ticket_name):
        if ticket_name == '1':
            new_card = ChargeableCard()
            return new_card
        elif ticket_name == '2':
            new_card = ExpirationCard
            return new_card
        else:
            new_card = DisposableTicket
            return new_card
