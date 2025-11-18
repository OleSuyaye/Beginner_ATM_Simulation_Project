balance = 0

menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))

while menu != 4:
    if menu == 1:
        deposit = int(input("How much do you want to deposit? "))
        balance = deposit + balance
        if deposit:
            follow_up = input("Do you want anything else, Y/N? ")
            if follow_up == "Y":
                menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))
            else:
                break
        else:
            break

    elif menu == 2:
        withdraw = int(input("How much do you want to withdraw? "))
        balance = balance - withdraw
        if withdraw:
            follow_up = input("Do you want anything else, Y/N? ")
            if follow_up == "Y":
                menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))
            else:
                break
        else:
            break
    elif menu == 3:
        print(f"Your balance is {balance}")
        follow_up = input("Do you want anything else, Y/N? ")
        if follow_up == "Y":
            menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))
        else:
            break
    else:
        print("Welcome again!")
        break

if menu == 1:
    print(f"After your deposit, you final balance is {balance}")
elif menu == 2:
    print(f"After your withdrawal, you final balance is {balance}")
elif menu == 3:
    print(f"Your balance is {balance}")








