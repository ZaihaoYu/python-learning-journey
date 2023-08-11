import datetime


def validate(func):
    def wrapper(self, *args, **kwargs):
        amount = str(args[0])
        # 123.456 , 100.01 , 100  index .
        index = amount.index(".")
        if len(amount) - index - 1 > 2:
            print("The input format is wrong, save up to two digits after the decimal point")
        else:
            func(self, *args, **kwargs)

    return wrapper


class Bank(object):
    account_log = []

    def __init__(self, name):
        self.name = name

    @validate
    def deposit(self, amount):
        user.balance += amount
        self.write_log("deposit", amount)

    @validate
    def withdrawal(self, amout):
        if amount > user.balance:
            print("Insufficient balance")
        else:
            user.balance -= amount
        self.write_log("withdrawal", amount)

    def write_log(self, type, amount):
        now = datetime.datetime.now()
        create_time = now.strftime("%Y-%m-%d %H:%M:%S")
        data = [self.name, user.username, create_time, type, amount, f"{user.balance:.2f}"]
        Bank.account_log.append(data)


class JPMorgan(Bank):
    def __init__(self, name):
        self.name = name


class Mitusi(Bank):
    def __init__(self, name):
        self.name = name


class User(object):
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def print_log(self):
        print(Bank.account_log)


bank = JPMorgan("JPMorgan")
user = User("Brandon", 1000)


def show_menu():
    menu = """"
menu：
0；Quit
1：Deposit
2：Withdrawal 
3；Print transaction information
        """
    print(menu)


while True:
    show_menu()
    num = int(input("Please enter according to the menu number： "))
    if num == 0:
        print("You are logged out")
        break
    elif num == 1:
        print("Deposit")
        amount = float(input("Please enter the deposit amount:"))
        bank.deposit(amount)
        print(f'Current balance:{user.balance:.2f}')
    elif num == 2:
        print("Withdrawal:")
        amount = float(input("Please enter the payment amount:"))
        bank.withdrawal(amount)
        print(f'Current balance:{user.balance:.2f}')
    elif num == 3:
        print("Print transaction information")
        user.print_log()
    else:
        print("Input error")
