import pickle
import random
from glob import glob
from admin import *
from clear import clear
from menu import *


def run():
    while 1:
        clear()
        print(Menu.metro_menu)
        for v in enumerate(Menu.first_page_menu):
            print(f'|{v[0] + 1}. {v[1]}|')
        user_input = int(input('enter your command: '))
        if user_input == 1:
            clear()
            print('---- Registration ----')
            fname = input('Enter your firstname: ')
            lname = input('Enter your lastname: ')
            nat_code = input('Enter your national code(must be 10 char): ')
            date_of_birth = input('Enter your date of birth: ')
            password = input('Enter backup password(at least 1 number, 1 uppercase, 8 character): ')
            try:
                assert name_validation(fname), 'Enter valid name'
                assert name_validation(lname), 'Enter valid name'
                assert national_code_validation(nat_code), 'Enter valid code'
                assert password_validation(password), 'Enter valid password'
                new_user = User(fname, lname, nat_code, date_of_birth, password)
                with open(f'Users/{new_user.user_id}.pickle', 'wb') as user:
                    pickle.dump(new_user, user)
                clear()
                print('---- welcome ----')
                input(f'You registered successful\nyour id is: {new_user.user_id}\nyour bank account ID: '
                      f'{new_user.bank_account.bank_account_id}')
            except AssertionError as e:
                input(e)
        elif user_input == 2:
            clear()
            print('---- Login ----')
            user_id = input('Enter your ID(Forgot ID? Enter (y)): ')
            if user_id == 'y':
                user_obj = []
                forgot_status = True
                for file in glob('Users/*.pickle'):
                    with open(file, 'rb') as user:
                        while 1:
                            try:
                                content = pickle.load(user)
                                user_obj.append(content)
                            except EOFError:
                                break
                while forgot_status:
                    clear()
                    print('---- Forgot ID ----')
                    national_code = input('Enter your national code: ')
                    f_password = input('Enter your password: ')
                    for user in user_obj:
                        if user.national_code == national_code and user.backup_pass == f_password:
                            clear()
                            print('---- ID ----')
                            input(f'Your id is: {user.user_id}')
                            forgot_status = False
                            break
                    else:
                        clear()
                        print('---- ID ----')
                        input('Wrong national code or password')
            else:
                try:
                    with open(f'Users/{user_id}.pickle', 'rb') as user:
                        logged_user: User = pickle.load(user)
                    while 1:
                        clear()
                        print(f'---- {logged_user.fname} {logged_user.lname} ----')
                        for v in enumerate(Menu.login_menu):
                            print(f'|{v[0] + 1}. {v[1]}|')
                        lg_input = int(input('Enter your desire: '))
                        if lg_input == 1:
                            clear()
                            print('---- Bank Account Management ----')
                            for v in enumerate(Menu.bank_account_menu):
                                print(f'|{v[0] + 1}. {v[1]}|')
                            bank_input = int(input('Enter your desire: '))
                            if bank_input == 1:
                                clear()
                                print('---- Deposit ----')
                                bank_id = int(input('Enter your bank ID: '))
                                if logged_user.bank_account.bank_account_id == bank_id:
                                    try:
                                        amount = int(input('Enter amount: '))
                                        logged_user.bank_account.deposit(amount)
                                    except AssertionError as e:
                                        input(e)
                                else:
                                    input('Bank ID was wrong!')
                            elif bank_input == 2:
                                clear()
                                print('---- Withdraw ----')
                                bank_id = int(input('Enter your bank ID: '))
                                if logged_user.bank_account.bank_account_id == bank_id:
                                    try:
                                        amount = int(input('Enter amount: '))
                                        logged_user.bank_account.withdraw(amount)
                                    except AssertionError as e:
                                        input(e)
                                else:
                                    input('Bank ID was wrong!')
                            elif bank_input == 3:
                                clear()
                                print('---- Balance ----')
                                bank_id = int(input('Enter your bank ID: '))
                                if logged_user.bank_account.bank_account_id == bank_id:
                                    try:
                                        input(logged_user.bank_account.show_balance(
                                            f'{logged_user.fname} {logged_user.lname}'))
                                    except AssertionError as e:
                                        input(e)
                                else:
                                    input('Bank ID was wrong!')
                            else:
                                break
                        elif lg_input == 2:
                            clear()
                            print('---- Buy Ticket ----')
                            for v in enumerate(Menu.buy_ticket_menu):
                                print(f'|{v[0] + 1}. {v[1]}|')
                            buy_input = int(input('Enter your desire: '))
                            if buy_input == 1:
                                ticket_lists = []
                                for file in glob('Tickets/Chargeable/*.pickle'):
                                    with open(file, 'rb') as ticket:
                                        content = pickle.load(ticket)
                                        if content.user is None:
                                            ticket_lists.append(content)

                                try:
                                    if len(ticket_lists) == 0:
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Chargeable/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                        input(f'card_id: {t.ticket_id}')

                                except Exception as e:
                                    input(e)

                            elif buy_input == 2:
                                ticket_lists = []
                                for file in glob('Tickets/Disposable/*.pickle'):
                                    with open(file, 'rb') as ticket:
                                        content = pickle.load(ticket)
                                        if content.user is None:
                                            ticket_lists.append(content)
                                try:
                                    if len(ticket_lists) == 0:
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Disposable/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                        input(f'card_id: {t.ticket_id}')

                                except Exception as e:
                                    input(e)
                            elif buy_input == 3:
                                ticket_lists = []
                                for file in glob('Tickets/Expire/*.pickle'):
                                    with open(file, 'rb') as ticket:
                                        content = pickle.load(ticket)
                                        if content.user is None:
                                            ticket_lists.append(content)

                                try:
                                    if len(ticket_lists) == 0:
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Expire/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                        input(f'card_id: {t.ticket_id}')

                                except Exception as e:
                                    input(e)
                            else:
                                break
                        elif lg_input == 3:
                            try:
                                clear()
                                print('---- Usage Ticket ----')
                                for v in enumerate(logged_user.ticket_list):
                                    print(f'|{v[0] + 1}. {v[1]}|')
                                ticket_choose = int(input('Choose Ticket: '))
                                if isinstance(logged_user.ticket_list[ticket_choose - 1], ChargeableCard):
                                    logged_user.ticket_list[ticket_choose - 1].withdraw(0.5)
                                    input('Have good travel')
                                elif isinstance(logged_user.ticket_list[ticket_choose - 1], DisposableTicket):
                                    logged_user.ticket_list[ticket_choose - 1].withdraw()
                                    input('Have good travel')
                                    logged_user.ticket_list.remove(logged_user.ticket_list[ticket_choose - 1])
                                elif isinstance(logged_user.ticket_list[ticket_choose - 1], ExpirationCard):
                                    assert logged_user.ticket_list[ticket_choose - 1].expire_date > \
                                           logged_user.ticket_list[ticket_choose - 1].expire(), 'Your Card Was Expired'
                                    logged_user.ticket_list[ticket_choose - 1].withdraw(0.75)
                                    input('Have good travel')
                                    if logged_user.ticket_list[ticket_choose - 1].balance == 0 or \
                                            logged_user.ticket_list[ticket_choose - 1].expire_date == \
                                            logged_user.ticket_list[ticket_choose - 1].expire():
                                        logged_user.ticket_list.remove(logged_user.ticket_list[ticket_choose - 1])
                                else:
                                    break
                            except Exception as e:
                                input(e)
                        elif lg_input == 4:
                            clear()
                            print('---- Charge Card ----')
                            for ticket in enumerate(logged_user.ticket_list):
                                if isinstance(ticket[1], ChargeableCard):
                                    print(f'|{ticket[0] + 1}. {ticket[1]}|')
                            choose = int(input('Choose your card: '))
                            amount = int(input('amount:\n1.10\n2.20\n3.50\n4.100\nEnter: '))
                            price_list = [10, 20, 50, 100]
                            logged_user.ticket_list[choose - 1].deposit(price_list[amount - 1])
                            input(f'Your Charge was successful\ncredit: {logged_user.ticket_list[choose - 1].balance}')
                        elif lg_input == 5:
                            clear()
                            print('---- Ticket List ----')
                            if len(logged_user.ticket_list) == 0:
                                input('You dont have ticket')
                            else:
                                for i in logged_user.show_ticket_list():
                                    print(i)
                                input()

                        elif lg_input == 6:
                            clear()
                            print('---- INFO ----')
                            input(logged_user)
                        elif lg_input == 7:
                            with open(f'Users/{logged_user.user_id}.pickle', 'wb') as user:
                                pickle.dump(logged_user, user)
                            break

                except FileNotFoundError:
                    input('User Not Found!')

        elif user_input == 3:
            clear()
            admin_id = input('Enter your ID: ')
            try:
                with open(f'Admins/{admin_id}.pickle', 'rb') as admin:
                    logged_admin: Admin = pickle.load(admin)
                adm_menu = ['Register New Admin',
                            'EXIT']
                if admin_id == '907823ac-0858-4683-b972-26fa8794a1f7':
                    for v in enumerate(adm_menu):
                        print(f'|{v[0] + 1}. {v[1]}|')
                    cmd = input('Choose: ')
                    if cmd == '1':
                        fname = input('Enter your firstname: ')
                        lname = input('Enter your lastname: ')
                        nat_code = input('Enter your national code(must be 10 char): ')
                        date_of_birth = input('Enter your date of birth: ')
                        password = input('Enter backup password(at least 1 number, 1 uppercase, 8 character): ')
                        try:
                            assert name_validation(fname), 'Enter valid name'
                            assert name_validation(lname), 'Enter valid name'
                            assert national_code_validation(nat_code), 'Enter valid code'
                            assert password_validation(password), 'Enter valid password'
                            new_admin = Admin(fname, lname, nat_code, date_of_birth, password)
                            with open(f'Admins/{new_admin.user_id}.pickle', 'wb') as n_admin:
                                pickle.dump(new_admin, n_admin)
                            clear()
                            print('---- welcome ----')
                            input(f'You registered successful\nyour id is: {new_admin.user_id}\nyour bank account ID: '
                                  f'{new_admin.bank_account.bank_account_id}')
                        except AssertionError as e:
                            input(e)
                    else:
                        break
                else:
                    while 1:
                        clear()
                        print('---- Admin page ----')
                        for v in enumerate(Menu.admin_menu):
                            print(f'|{v[0] + 1}. {v[1]}|')
                        cmd = input('CHOOSE: ')
                        if cmd == '1':
                            pass
                        elif cmd == '2':
                            pass
                        elif cmd == '3':
                            while 1:
                                clear()
                                print('---- CREATE TICKET ----')
                                for v in enumerate(Menu.buy_ticket_menu):
                                    print(f'|{v[0] + 1}. {v[1]}|')
                                admin_input = input('What is your Desire: ')
                                if admin_input == '1':
                                    clear()
                                    print('---- Chargeable Card ----')
                                    new_ticket = logged_admin.create_ticket(admin_input)
                                    with open(f'Tickets/Chargeable/{new_ticket.ticket_id}.pickle', 'wb') as ticket:
                                        pickle.dump(new_ticket, ticket)
                                    input(new_ticket)
                                elif admin_input == '2':
                                    clear()
                                    print('---- Disposable Card ----')
                                    new_ticket = logged_admin.create_ticket(admin_input)
                                    with open(f'Tickets/Disposable/{new_ticket.ticket_id}.pickle', 'wb') as ticket:
                                        pickle.dump(new_ticket, ticket)
                                    input(new_ticket)
                                elif admin_input == '3':
                                    clear()
                                    print('---- Expiration Ticket ----')
                                    new_ticket = logged_admin.create_ticket(admin_input)
                                    with open(f'Tickets/Expire/{new_ticket.ticket_id}.pickle', 'wb') as ticket:
                                        pickle.dump(new_ticket, ticket)
                                    input(new_ticket)
                                else:
                                    break
                        elif cmd == '4':
                            pass
                        elif cmd == '5':
                            while 1:
                                clear()
                                print('---- Ticket list ----')
                                for v in enumerate(Menu.buy_ticket_menu):
                                    print(f'|{v[0] + 1}. {v[1]}|')
                                admin_input = input('What is your Desire: ')
                                ticket_list = []
                                if admin_input == '1':
                                    clear()
                                    print('---- Chargeable Ticket ----')
                                    try:
                                        n = 1
                                        for file in glob('Tickets/Chargeable/*.pickle'):
                                            with open(file, 'rb') as ticket:
                                                content = pickle.load(ticket)
                                            print(f'{n}: {content.ticket_id}')
                                            n += 1
                                        input()
                                    except FileNotFoundError:
                                        input('We dont have tickets!!')

                                elif admin_input == '2':
                                    clear()
                                    print('---- Disposable Ticket ----')
                                    try:
                                        n = 1
                                        for file in glob('Tickets/Disposable/*.pickle'):
                                            with open(file, 'rb') as ticket:
                                                content = pickle.load(ticket)
                                            print(f'{n}: {content.ticket_id}')
                                            n += 1
                                        input()
                                    except FileNotFoundError:
                                        input('We dont have ticket!!')
                                elif admin_input == '3':
                                    clear()
                                    print('---- Expireable Ticket ----')
                                    try:
                                        n = 1
                                        for file in glob('Tickets/Expire/*.pickle'):
                                            with open(file, 'rb') as ticket:
                                                content = pickle.load(ticket)
                                            print(f'{n}: {content.ticket_id}')
                                            n += 1
                                        input()
                                    except FileNotFoundError:
                                        input('We dont have ticket!!')
                                else:
                                    break
                        else:
                            break
            except FileNotFoundError:
                input('User Not Found!')

        else:
            break


if __name__ == '__main__':
    run()

# 6087099462
# 403b611d-da8b-4376-aa64-a10be8ae31fe
# 4531473070
# 4c7ef1c3-0f37-441e-907d-35ed85bed37d
# adminID = 907823ac-0858-4683-b972-26fa8794a1f7
# ali_admin = 15defe5d-e6ca-461f-808e-67cef6453099
# chargeable = bc7b77d7-948e-47ba-bd65-ae0cf3ee3404, 220182c1-58c9-4fc0-9880-e7616c039f1f
# excard = 318ef8ff-e426-4ccf-ba49-c3eeb99c24fd
# dsticket = cf7b3805-9734-4be4-a7d9-11a35289ce47

# 49cba062-7214-40d9-95a2-382d53ba7bbb
# 6488537414