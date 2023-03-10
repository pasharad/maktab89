import pickle
import random
from glob import glob
from admin import *
from clear import clear
from menu import *
import metro_log


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
                metro_log.user_logger.info(f'User created, UserID: {new_user.user_id}')
                clear()
                print('---- welcome ----')
                input(f'You registered successful\nyour id is: {new_user.user_id}\nyour bank account ID: '
                      f'{new_user.bank_account.bank_account_id}')
            except AssertionError as e:
                metro_log.error_logger.error(f'Register failed by Error: {e}')
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
                    metro_log.user_logger.info(f'User {logged_user.user_id} logged in!')
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
                                        metro_log.user_logger.info(f'User {logged_user.user_id} '
                                                                   f'Deposit {amount}!')
                                    except Exception as e:
                                        metro_log.error_logger.error(f'Deposit failed by Error: {e}')
                                        input(e)
                                else:
                                    metro_log.error_logger.error(f'User {logged_user.user_id} Enter wrong Bank ID')
                                    input('Bank ID was wrong!')
                            elif bank_input == 2:
                                clear()
                                print('---- Withdraw ----')
                                bank_id = int(input('Enter your bank ID: '))
                                if logged_user.bank_account.bank_account_id == bank_id:
                                    try:
                                        amount = int(input('Enter amount: '))
                                        logged_user.bank_account.withdraw(amount)
                                        metro_log.user_logger.info(f'User {logged_user.user_id} Withdraw {amount}')
                                    except Exception as e:
                                        metro_log.error_logger.error(f'Withdraw failed by Error {e}')
                                        input(e)
                                else:
                                    metro_log.error_logger.error(f'User {logged_user.user_id} Enter wrong Bank ID')
                                    input('Bank ID was wrong!')
                            elif bank_input == 3:
                                clear()
                                print('---- Balance ----')
                                bank_id = int(input('Enter your bank ID: '))
                                if logged_user.bank_account.bank_account_id == bank_id:
                                    try:
                                        input(logged_user.bank_account.show_balance(
                                            f'{logged_user.fname} {logged_user.lname}'))
                                        metro_log.user_logger.info(f'User {logged_user.user_id} check Balance!')
                                    except Exception as e:
                                        metro_log.error_logger.error(f'Show Balance failed by Error {e}')
                                        input(e)
                                else:
                                    metro_log.error_logger.error(f'User {logged_user.user_id} Enter wrong Bank ID')
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
                                        metro_log.error_logger.error('Card was not created!!!')
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        metro_log.user_logger.info(f'User {logged_user.user_id} Withdraw {t.cost}')
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Chargeable/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                        metro_log.user_logger.info(f'User {logged_user.user_id} Buy Chargeable Card '
                                                                   f'{t.ticket_id}')
                                        input(f'card_id: {t.ticket_id}')

                                except Exception as e:
                                    metro_log.error_logger.error(f'User: {logged_user.user_id}'
                                                                 f', Buy ticket failed by Error: {e}')
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
                                        metro_log.error_logger.error('Card was not created!!!')
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        metro_log.user_logger.info(f'User {logged_user.user_id} Withdraw {t.cost}')
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Disposable/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                            metro_log.user_logger.info(
                                                f'User {logged_user.user_id} Buy Chargeable Card '
                                                f'{t.ticket_id}')
                                        input(f'card_id: {t.ticket_id}')

                                except Exception as e:
                                    metro_log.error_logger.error(f'User: {logged_user.user_id}'
                                                                 f', Buy ticket failed by Error: {e}')
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
                                        metro_log.error_logger.error('Card was not created!!!')
                                        input('We dont have card!!')
                                    else:
                                        t = random.choice(ticket_lists)
                                        clear()
                                        logged_user.bank_account.withdraw(t.cost)
                                        metro_log.user_logger.info(f'User {logged_user.user_id} Withdraw {t.cost}')
                                        print('Your action was successful')
                                        t.user = logged_user.user_id
                                        logged_user.ticket_list.append(t)
                                        with open(f'Tickets/Expire/{t.ticket_id}.pickle', 'wb') as ticket:
                                            pickle.dump(t, ticket)
                                        metro_log.user_logger.info(
                                            f'User {logged_user.user_id} Buy Chargeable Card '
                                            f'{t.ticket_id}')
                                        input(f'card_id: {t.ticket_id}')
                                except Exception as e:
                                    metro_log.error_logger.error(f'User: {logged_user.user_id}'
                                                                 f', Buy ticket failed by Error: {e}')
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
                                    metro_log.user_logger.info(f'User {logged_user.user_id} use Chargeable Card'
                                                               f'{logged_user.ticket_list[ticket_choose - 1].ticket_id}'
                                                               )
                                    input('Have good travel')
                                elif isinstance(logged_user.ticket_list[ticket_choose - 1], DisposableTicket):
                                    logged_user.ticket_list[ticket_choose - 1].withdraw()
                                    metro_log.user_logger.info(f'User {logged_user.user_id} use Disposable Ticket'
                                                               f'{logged_user.ticket_list[ticket_choose - 1].ticket_id}'
                                                               )
                                    input('Have good travel')
                                    logged_user.ticket_list[ticket_choose - 1].delete()
                                    logged_user.ticket_list.remove(logged_user.ticket_list[ticket_choose - 1])
                                elif isinstance(logged_user.ticket_list[ticket_choose - 1], ExpirationCard):
                                    assert logged_user.ticket_list[ticket_choose - 1].expire_date > \
                                           logged_user.ticket_list[ticket_choose - 1].expire(), 'Your Card Was Expired'
                                    logged_user.ticket_list[ticket_choose - 1].withdraw(0.75)
                                    metro_log.user_logger.info(f'User {logged_user.user_id} use Expiration Card'
                                                               f'{logged_user.ticket_list[ticket_choose - 1].ticket_id}'
                                                               )
                                    input('Have good travel')
                                    if logged_user.ticket_list[ticket_choose - 1].balance == 0 or \
                                            logged_user.ticket_list[ticket_choose - 1].expire_date == \
                                            logged_user.ticket_list[ticket_choose - 1].expire():
                                        logged_user.ticket_list[ticket_choose - 1].delete()
                                        logged_user.ticket_list.remove(logged_user.ticket_list[ticket_choose - 1])
                                else:
                                    break
                            except Exception as e:
                                metro_log.error_logger.error(f'Ticket Usage failed by Error {e}')
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
                            logged_user.bank_account.withdraw(price_list[amount - 1])
                            metro_log.user_logger.info(f'User {logged_user.user_id} Charging Card '
                                                       f'Card ID {logged_user.ticket_list[choose - 1].ticket_id}'
                                                       f'amount {price_list[amount - 1]}')
                            logged_user.ticket_list[choose - 1].deposit(price_list[amount - 1])
                            metro_log.user_logger.info(f'Card ID {logged_user.ticket_list[choose - 1].ticket_id} was '
                                                       f'charged')
                            input(f'Your Charge was successful\ncredit: {logged_user.ticket_list[choose - 1].balance}')
                        elif lg_input == 5:
                            clear()
                            print('---- Ticket List ----')
                            if len(logged_user.ticket_list) == 0:
                                metro_log.error_logger.error(f'User {logged_user.user_id} Dont have Tickets!!')
                                input('You dont have ticket')
                            else:
                                for i in logged_user.show_ticket_list():
                                    print(i)
                                metro_log.user_logger.info(f'User {logged_user.user_id} Check Ticket list!!')
                                input()

                        elif lg_input == 6:
                            clear()
                            print('---- INFO ----')
                            metro_log.user_logger.info(f'User {logged_user.user_id} Check INFO!!!')
                            input(logged_user)
                        elif lg_input == 7:
                            with open(f'Users/{logged_user.user_id}.pickle', 'wb') as user:
                                pickle.dump(logged_user, user)
                            metro_log.user_logger.info(f'User {logged_user.user_id} logged out!')
                            break

                except FileNotFoundError:
                    metro_log.error_logger.error('Can not login/ User Not Found!!!')
                    input('User Not Found!')

        elif user_input == 3:
            clear()
            admin_id = input('Enter your ID: ')
            try:
                with open(f'Admins/{admin_id}.pickle', 'rb') as admin:
                    logged_admin: Admin = pickle.load(admin)
                adm_menu = ['Register New Admin',
                            'EXIT']
                if admin_id == '0cc0a947-bd91-4228-b7b0-0fb39944a90c':
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
                            metro_log.admin_logger.info(f'Admin {new_admin.user_id} is created!!!')
                            clear()
                            print('---- welcome ----')
                            input(f'You registered successful\nyour id is: {new_admin.user_id}\nyour bank account ID: '
                                  f'{new_admin.bank_account.bank_account_id}')
                        except AssertionError as e:
                            metro_log.error_logger.error(f'Admin Registration failed by Error {e}')
                            input(e)
                    else:
                        break
                else:
                    metro_log.admin_logger.info(f'Admin {logged_admin.user_id} logged in!!!')
                    while 1:
                        clear()
                        print('---- Admin page ----')
                        for v in enumerate(Menu.admin_menu):
                            print(f'|{v[0] + 1}. {v[1]}|')
                        cmd = input('CHOOSE: ')
                        if cmd == '1':
                            clear()
                            print('---- Make New Travel ----')
                            travel_id = input('Enter Travel ID: ')
                            origin = input('Enter origin: ')
                            destination = input('Enter Destination: ')
                            logged_admin.make_transport(travel_id, origin, destination)
                            metro_log.admin_logger.info(f'Travel {travel_id} made by Admin {logged_admin.user_id} ')
                        elif cmd == '2':
                            clear()
                            print('---- Edit Travel ----')
                            logged_admin.check_transport()
                            transport_list = []
                            for transport in logged_admin.transport:
                                if transport == 'Unavailable':
                                    transport_list.append(transport)
                            if len(transport_list) == 0:
                                input('Are Transport is Available')
                            else:
                                for i in enumerate(transport_list):
                                    print(f'{i[0] + 1}\n{i[1]}')
                                travel = int(input('Choose travel for change: '))
                                travel_id = input('Enter Travel ID: ')
                                origin = input('Enter origin: ')
                                destination = input('Enter Destination: ')
                                logged_admin.edit_transport(transport_list[travel - 1], travel_id, origin,
                                                            destination)
                                metro_log.admin_logger.info(f'Travel {travel_id} Edited by Admin {logged_admin.user_id}'
                                                            )
                        elif cmd == '3':
                            clear()
                            print('---- Show Available Travel ----')
                            metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Check  Travels')
                            logged_admin.check_transport()
                            if len(logged_admin.transport) == 0:
                                input('We Dont Have Any Available Transport')
                            else:
                                for transport in enumerate(logged_admin.transport):
                                    if transport[1].status == 'Available':
                                        print(f'{transport[0] + 1}\n{transport[1]}')
                                input()
                        elif cmd == '4':
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
                                    metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Create Chargeable Card')
                                    input(new_ticket)
                                elif admin_input == '2':
                                    clear()
                                    print('---- Disposable Card ----')
                                    new_ticket = logged_admin.create_ticket(admin_input)
                                    with open(f'Tickets/Disposable/{new_ticket.ticket_id}.pickle', 'wb') as ticket:
                                        pickle.dump(new_ticket, ticket)
                                    metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Create Disposable Card')
                                    input(new_ticket)
                                elif admin_input == '3':
                                    clear()
                                    print('---- Expiration Card ----')
                                    new_ticket = logged_admin.create_ticket(admin_input)
                                    with open(f'Tickets/Expire/{new_ticket.ticket_id}.pickle', 'wb') as ticket:
                                        pickle.dump(new_ticket, ticket)
                                    metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Create Expiration Card')
                                    input(new_ticket)
                                else:
                                    break
                        elif cmd == '5':
                            clear()
                            print('---- Ban User ----')
                            user_id = input('Enter User ID To Ban: ')
                            logged_admin.delete(user_id)
                            metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Ban User {user_id}!!!')
                            input('User Banned!!!')
                        elif cmd == '6':
                            metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Check Card Created!!!')
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
                                        metro_log.error_logger.error('Show card created but Any Card has been created!!'
                                                                     '!')
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
                                        metro_log.error_logger.error('Show card created but Any Card has been created!!'
                                                                     '!')
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
                                        metro_log.error_logger.error('Show card created but Any Card has been created!!'
                                                                     '!')
                                        input('We dont have ticket!!')
                                else:
                                    break
                        else:
                            with open(f'Admins/{logged_admin.user_id}.pickle', 'wb') as n_admin:
                                pickle.dump(logged_admin, n_admin)
                            metro_log.admin_logger.info(f'Admin {logged_admin.user_id} Logged out!!!')
                            break
            except FileNotFoundError:
                metro_log.error_logger.error('Any Admin has been found!!!')
                input('Admin Not Found!')

        else:
            break


if __name__ == '__main__':
    run()
