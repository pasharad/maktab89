import re


def username_validation(username:str) -> str:
    assert username.isalpha(), 'Enter correct username!'
    return username

def password_validation(password:str) -> str:
    assert re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$', password), 'Enter valid password!'
    return password

def email_validation(email:str) -> str:
    assert re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
                    r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", 
                    email),'Enter valid email!'
    return email

