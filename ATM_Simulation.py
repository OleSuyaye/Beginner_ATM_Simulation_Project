print("______WELCOME TO MY BEGINNER ATM SIMULATION PYTHON PROJECT_______")
balance = 0

menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))

while menu:
    if menu == 1:
        deposit = int(input("How much do you want to deposit in $? "))
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
        withdraw = int(input("How much do you want to withdraw in $? "))
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
        print(f"Your balance is ${balance}")
        follow_up = input("Do you want anything else, Y/N? ")
        if follow_up == "Y":
            menu = int(input("Choose a number: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))
        else:
            break

    elif menu == 4:
        print("Thank for using our services!")
        break

    elif menu > 4:
        menu = int(input("You have to chose a number from the following: 1. Deposit, 2.Withdraw, 3. Check Balance, 4. Exit: "))

    else:
        print("Welcome again!")
        break
print(f"Thank you for using our services! Your Balance is now at ${balance}")









