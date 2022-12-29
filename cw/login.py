import re
from os import name as os_name, system as terminal


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


class User:
    usernames = []
    users = []

    def __init__(self, fname, lname, phone, email, username, password):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.users.append(self)

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @phone.setter
    def phone(self, phone):
        assert re.match(r"^\+98\d{10}", phone), "enter valid phone"
        self.__phone = phone

    @password.setter
    def password(self, password):
        assert re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password), "enter valid password"
        self.__password = password

    @username.setter
    def username(self, username):
        assert username not in User.usernames, "this username already taken"
        User.usernames.append(username)
        self.__username = username

    @email.setter
    def email(self, email):
        assert re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
                        r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
                        r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", email), "enter valid email"
        self.__email = email

    @staticmethod
    def login(username, password,users):
        for user in users:
            if user.username == username and user.password == password:
                # print(f"welcome {user.fname} {user.lname}")
                return user
        # print("username or password is wrong!!!")
        return False

    def __repr__(self):
        return f"{self.fname} {self.lname}"


if __name__ == "__main__":
    current_user = "no one logged in!!!"
    while True:
        clear()
        print(current_user,"\n\n")
        cmd = int(input("====menu====\n\n1. login\n2. register\n3. exit\n\n> "))
        if cmd == 1:
            clear()
            username = input("enter username: ")
            password = input("enter password: ")
            user = User.login(username, password,User.users)
            if user:
                input(f"welcome {user.fname} {user.lname}")
            else:
                input("username or password is wrong!!!")
            if user:
                current_user = user
        elif cmd == 2:
            clear()
            try:
                new_user = User(input("first name: "), input("last name: "), input("phone number: "),
                            input("email: "), input("username: "), input("password: "))
            except AssertionError as msg:
                clear()
                input(msg)
        else:
            clear()
            break
