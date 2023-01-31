class Menu:
    first_page_menu = [
        'Register New User',
        'Log in as User',
        'Log in as Administrator',
        'Exit']

    login_menu = [
        'Bank Account Management',
        'Buy Ticket',
        'Use_ticket',
        'Ticket List',
        'Account Info',
        'Log out']

    bank_account_menu = [
        'Deposit',
        'Withdraw',
        'Show Balance',
        'Go back...']

    buy_ticket_menu = [
        'Chargeable',
        'Disposable(you can use it only once)',
        'Date Expire']

    admin_menu = [
        'Make transport',
        'Edit transport',
        'logout'
    ]

    metro_menu = '''
    __  __      _
|  \/  | ___| |_ _ __ ___
| |\/| |/ _ \ __| '__/ _ 
| |  | |  __/ |_| | | (_) |
|_|  |_|\___|\__|_|  \___/\n
'''

# menu = Menu
# for v in enumerate(menu.buy_ticket_menu):
#     print(f'|{v[0]+1}. {v[1]}|')
