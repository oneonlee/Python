def deposit_function(deposit, balance):
    while True:
        try:
            deposit = int(input("How much do you want to deposit?"))
            if type(deposit) == int:
                break
        except ValueError:
            pass

    print("You deposited " + str(deposit) + " won")
    balance = balance + deposit
    return balance


def withdrawal_function(withdrawal, balance):
    withdrawal = int(input("How much do you want to withdraw?"))
    if withdrawal > balance:
        print("You've withdrawn " + str(withdrawal) + " won")
        print("But you only have " + str(balance) + " won")
        return balance
    else:
        print("You've withdrawn " + str(withdrawal) + " won")
        balance = balance - withdrawal
        return balance


def balance_function(balance):
    print("Your current balance is " + str(balance) + " won")
    return balance


def bank():
    deposit = 0
    withdrawal = 0
    balance = 0

    while True:
        name = input("Deposit(d) or withdrawal(w) or balance check(C)??")
        if (name == "d"):
            balance = deposit_function(deposit, balance)
            continue
        if (name == "w"):
            balance = withdrawal_function(withdrawal, balance)
            continue
        if (name == "c"):
            balance_function(balance)
            # print(balance)
            continue
        if (name == "q"):
            break


bank()
