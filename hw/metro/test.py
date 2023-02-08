import unittest
import admin


class BankAccountTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.account = admin.BankAccount(100)

    def test_attrib(self):
        self.assertNotEqual(self.account.bank_account_id, None)
        self.assertNotEqual(self.account.bank_account_id, None)
        self.assertNotEqual(self.account.bank_account_id, None)

    def test_deposit(self):
        self.assertEqual(self.account.balance, 100)
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
        with self.assertRaises(AssertionError) as context:
            self.account.withdraw(60)
        self.assertEqual(str(context.exception), 'your balance is not enough!!!')

    def test_balance(self):
        self.account.show_balance('pasha')
        self.assertEqual(self.account.balance, 99)


class TicketTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.chargeable_card = admin.ChargeableCard()
        self.disposable_ticket = admin.DisposableTicket()
        self.expire_card = admin.ExpirationCard()

    def test_chargeable(self):
        self.assertNotEqual(self.chargeable_card.ticket_id, None)
        self.assertNotEqual(self.chargeable_card.cost, None)
        self.assertNotEqual(self.chargeable_card.balance, None)
        self.assertNotEqual(self.chargeable_card.creation_date, None)
        self.chargeable_card.deposit(10)
        self.assertEqual(self.chargeable_card.balance, 10)
        self.chargeable_card.withdraw(0.5)
        self.assertEqual(self.chargeable_card.balance, 9.5)
        with self.assertRaises(AssertionError) as context:
            self.chargeable_card.withdraw(20)
        self.assertEqual(str(context.exception), 'your charge is not enough, please charge')

    def test_disposable(self):
        self.assertNotEqual(self.disposable_ticket.ticket_id, None)
        self.assertNotEqual(self.disposable_ticket.cost, None)
        self.assertNotEqual(self.disposable_ticket.balance, None)
        self.assertNotEqual(self.disposable_ticket.creation_date, None)
        self.disposable_ticket.withdraw()
        self.assertEqual(self.disposable_ticket.balance, 0)
        with self.assertRaises(AssertionError) as context:
            self.disposable_ticket.withdraw()
        self.assertEqual(str(context.exception), 'your ticket has been expired')

    def test_expire(self):
        self.assertNotEqual(self.expire_card.ticket_id, None)
        self.assertNotEqual(self.expire_card.cost, None)
        self.assertNotEqual(self.expire_card.balance, None)
        self.assertNotEqual(self.expire_card.creation_date, None)
        self.expire_card.withdraw(0.75)
        self.assertEqual(self.expire_card.balance, 49.25)
        with self.assertRaises(AssertionError) as context:
            self.expire_card.withdraw(50)
        self.assertEqual(str(context.exception), 'your card has been expired')


class UserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = admin.User('pasha', 'rad', '1234567890', '80', 'Pasha1234')
        self.ticket = admin.ChargeableCard()

    def test_item(self):
        self.assertNotEqual(self.user.user_id, None)
        self.assertNotEqual(self.user.fname, None)
        self.assertNotEqual(self.user.lname, None)
        self.assertNotEqual(self.user.date_of_birth, None)
        self.assertNotEqual(self.user.national_code, None)
        self.assertNotEqual(self.user.bank_account, None)

    def test_buy_ticket(self):
        self.user.buy_ticket(self.ticket)
        self.assertEqual(len(self.user.ticket_list), 1)


class AdminTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.admin = admin.Admin('admin', 'admin', '1234567890', '1', 'Admin1234')

    def test_item(self):
        self.assertNotEqual(self.admin.user_id, None)
        self.assertNotEqual(self.admin.fname, None)
        self.assertNotEqual(self.admin.lname, None)
        self.assertNotEqual(self.admin.date_of_birth, None)
        self.assertNotEqual(self.admin.national_code, None)
        self.assertNotEqual(self.admin.bank_account, None)

    def test_travel(self):
        self.admin.make_transport(1, 'tajrish', 'kahrizak')
        self.assertNotEqual(len(self.admin.transport), 0)

    def test_ticket(self):
        self.assertIsInstance(self.admin.create_ticket('1'), admin.ChargeableCard)
        self.assertIsInstance(self.admin.create_ticket('2'), admin.DisposableTicket)
        self.assertIsInstance(self.admin.create_ticket('3'), admin.ExpirationCard)


if __name__ == '__main__':
    unittest.main()
