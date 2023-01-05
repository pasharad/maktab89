import unittest
import bank_account


class Tests(unittest.TestCase):
    def test_fname(self):
        self.assertRaises(AssertionError, bank_account.Customer.cfname, '12233')

    def test_lname(self):
        self.assertRaises(AssertionError, bank_account.Customer.clname, '123334')

    def test_phone(self):
        self.assertRaises(AssertionError, bank_account.Customer.cphone, 'pasha')

    def test_email(self):
        self.assertRaises(AssertionError, bank_account.Customer.cemail, 'pasdsd2')


class Test_bank(unittest.TestCase):
    c1 = bank_account.Customer('pasha', 'rad', '09123344555', 'pasharad2231@gmail.com')
    b1 = bank_account.BankAccount(c1, 10000)

    def test_bal(self):
        self.assertRaises(AssertionError, self.b1.yechi, 100)

    def test_check_withdraw(self):
        self.assertRaises(AssertionError, self.b1.check_minimum_balance, '999')

    def test_withdraw(self):
        self.assertRaises(Exception, self.b1.withdraw, 1000000)

    def test_deposit(self):
        self.assertRaises(AssertionError, self.b1.deposit, 'kdoaskdo')

    def test_transfer(self):
        self.assertRaises(AssertionError, self.b1.transfer, 'b2', 'skdksldk')

    def test_wage(self):
        self.assertRaises(AssertionError, self.b1.change_wage, 'aksodkosd')

    def test_change_min_balance(self):
        self.assertRaises(AssertionError, self.b1.change_min_balance, 'akspdkspd')


if __name__ == '__main__':
    unittest.main()
