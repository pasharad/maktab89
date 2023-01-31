from clear import clear
from menu import *
from bank_account import *
from ticket import *
from user import *
import pickle
from glob import glob


def run():
    while 1:
        clear()
        print(Menu.metro_menu)
        for v in enumerate(Menu.first_page_menu):
            print(f'|{v[0]+1}. {v[1]}|')
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
                input(f'You registered successful\nyour id is: {new_user.user_id}')
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
                        logged_user = pickle.load(user)
                    while 1:
                        clear()
                        print(f'---- {logged_user.fname} {logged_user.lname} ----')
                        for v in enumerate(Menu.login_menu):
                            print(f'|{v[0] + 1}. {v[1]}|')
                        lg_input = int(input('Enter your desire: '))
                        if lg_input == 1:
                            pass
                        elif lg_input == 2:
                            pass
                        elif lg_input == 3:
                            pass
                        elif lg_input == 4:
                            pass
                        elif lg_input == 5:
                            pass
                        elif lg_input == 6:
                            pass

                except FileNotFoundError:
                    input('User Not Found!')

        elif user_input == 3:
            pass
        else:
            break


if __name__ == '__main__':
    run()


# 403b611d-da8b-4376-aa64-a10be8ae31fe