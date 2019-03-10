
def withdraw(balance):
    while True:
        try:
            amount = int(input("How much would you like to withdraw?"))
            return balance - amount
        except ValueError:
            print("That's not an number!")
            continue

def deposit(balance):
    while True:
        try:
            amount = int(input("How much would you like to deposit?"))
            return balance + amount
        except ValueError:
            print("That's not an number!")
            continue

def check_balance(balance):
    print(f"Your current balance is: ${balance}")

actions = {
    'deposit': deposit,
    'withdraw': withdraw,
    'check_balance': check_balance,
}

balance = 5000

print("Welcome to Chase bank.")
while True:
    action = input(f"What would you like to do?")
    if action == 'exit':
        break
    if not action in actions:
        print("That's not a valid action.")
        continue
    if action != 'check_balance':
        balance = actions[action](balance)

    check_balance(balance)

    another = input("Are you done?")
    if another.lower() in ['y', 'yes']:
        break


print("Have a nice day!")