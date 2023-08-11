import datetime

balance = 1000
account_log = []


def validate(func):
    def wrapper(*args, **kwargs):
        amount = str(args[0])
        index = amount.index(".")
        if len(amount) - index - 1 > 2:
            print("The input format is wrong, save up to two digits after the decimal point")
        else:
            func(*args, **kwargs)

    return wrapper

@validate
def deposit(amount):
    """
    Deposit
    :param amount:deposits
    :return:None
    """
    global balance
    balance += amount
    write_log(amount, "deposit")

@validate
def withdrawal(amount):
    """
    Withdrawal amount
    :param amount: withdrawal
    :return: None
    """
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
    write_log(amount, "withdrawal")


def write_log(amount, type):
    """
    Write Log
    :param amount: amount
    :param type: deposit or withdrawal
    :return: None
    """
    now = datetime.datetime.now()
    create_time = now.strftime("%Y-%m-%d %H:%M:%S")
    data = [create_time, type, amount, f"{balance:.2f}" ]
    account_log.append(data)


def print_log():
    """
    Print transaction information
    :return: Noun
    """
    print(account_log)


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
        deposit(amount)
        print(f'Current balance:{balance:.2f}')
    elif num == 2:
        print("Withdrawal:")
        amount = float(input("Please enter the payment amount:"))
        withdrawal(amount)
        print(f'Current balance:{balance:.2f}')
    elif num == 3:
        print("Print transaction information")
        print_log()
    else:
        print("Input error")
