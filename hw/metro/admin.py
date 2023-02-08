from user import *
from ticket import *
from datetime import datetime, timedelta


class Transportation:
    end_time: datetime

    def __init__(self, tr_id, origin, destination):
        self.tr_id = tr_id
        self.origin = origin
        self.destination = destination
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=30)
        self.status = 'Available'

    def __repr__(self):
        return f'ID: {self.tr_id}\nOrigin: {self.origin}\nDestination: {self.destination}'


class Admin(User):
    def __init__(self, fname, lname, nat_code, date_of_birth, password):
        super().__init__(fname, lname, nat_code, date_of_birth, password)
        self.transport = []

    def make_transport(self, tr_id, origin, destination):
        new_transport = Transportation(tr_id, origin, destination)
        self.transport.append(new_transport)

    @staticmethod
    def edit_transport(cls, tr_id, origin, destination):
        cls.tr_id = tr_id
        cls.origin = origin
        cls.destination = destination

    @staticmethod
    def create_ticket(ticket_name):
        if ticket_name == '1':
            new_card = ChargeableCard()
            return new_card
        elif ticket_name == '2':
            new_card = DisposableTicket()
            return new_card
        else:
            new_card = ExpirationCard()
            return new_card

    @staticmethod
    def delete(user_id):
        if os_name == 'nt':
            chdir('Users')
            terminal(f'del {user_id}.pickle')
            chdir('..')
        else:
            chdir('Users')
            terminal(f'rm {user_id}.pickle')
            chdir('..')

    def check_transport(self):
        time = datetime.now()
        for travel in self.transport:
            if travel.end_time <= time:
                travel.status = 'Unavailable'
