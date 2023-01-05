import unittest
import bank_account


class Tests(unittest.TestCase):
    c1 = bank_account.Customer('saleh', 'naseh', '09132244555', 'saleh@gmail.com')

    def test_fname(self):
        self.assertRaises(AssertionError, bank_account.Customer.cfname, '12233')
        self.assertEqual(self.c1.first_name, 'saleh')

    def test_lname(self):
        self.assertRaises(AssertionError, bank_account.Customer.clname, '123334')
        self.assertEqual(self.c1.last_name, 'naseh')
    def test_phone(self):
        self.assertRaises(AssertionError, bank_account.Customer.cphone, 'pasha')
        self.assertEqual(self.c1.phone,'09132244555')
    def test_email(self):
        self.assertRaises(AssertionError, bank_account.Customer.cemail, 'pasdsd2')
        self.assertEqual(self.c1.email, 'saleh@gmail.com')

class Test_bank(unittest.TestCase):

    def setUp(self) -> None:
        self.c1 = bank_account.Customer('pasha', 'rad', '09123344555', 'pasharad2231@gmail.com')
        self.c2 = bank_account.Customer('saleh', 'naseh', '09132244555', 'saleh@gmail.com')
        self.b1 = bank_account.BankAccount(self.c1, 10000)
        self.b2 = bank_account.BankAccount(self.c2,12000)
    def test_bal(self):
        self.assertRaises(AssertionError, self.b1.yechi, 100)

    def test_check_withdraw(self):
        self.assertRaises(AssertionError, self.b1.check_minimum_balance, '999')

    def test_withdraw(self):
        self.assertRaises(Exception, self.b1.withdraw, 1000000)
        self.b1.withdraw(1000)
        self.assertEqual(self.b1.get_balance(), 9000 - self.b1.WAGE_AMOUNT)

    def test_deposit(self):
        self.assertRaises(AssertionError, self.b1.deposit, 'kdoaskdo')
        self.b1.deposit(1000)
        self.assertEqual(self.b1.get_balance(), 11000 - self.b1.WAGE_AMOUNT)

    def test_transfer(self):
        self.assertRaises(AssertionError, self.b1.transfer, 'b2', 'skdksldk')
        print(self.b1.get_balance())
        self.b1.transfer(self.b2, 1000)
        print(self.b1.get_balance())
        self.assertEqual(self.b1.get_balance(), 9000 - self.b1.WAGE_AMOUNT)
        self.assertEqual(self.b2.get_balance(), 13000 - self.b1.WAGE_AMOUNT)

    def test_wage(self):
        self.assertRaises(AssertionError, self.b1.change_wage, 'aksodkosd')

    def test_change_min_balance(self):
        self.assertRaises(AssertionError, self.b1.change_min_balance, 'akspdkspd')


if __name__ == '__main__':
    unittest.main()
