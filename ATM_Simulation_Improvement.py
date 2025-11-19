print("______WELCOME TO MY BEGINNER ATM SIMULATION PYTHON PROJECT_______")
balance = 0

while True:
    # Ask for input as a string
    menu = input("Choose a number: 1. Deposit, 2. Withdraw, 3. Check Balance, 4. Exit: ")

    # Check if the input is a number
    if menu.isdigit():
        menu = int(menu)  # Convert to number safely

        if menu == 1:
            deposit = int(input("How much do you want to deposit in $? "))
            balance += deposit
            print(f"Your new balance is ${balance}")

        elif menu == 2:
            withdraw = int(input("How much do you want to withdraw in $? "))
            if withdraw > balance:
                print("You cannot withdraw more than your balance!")
            else:
                balance -= withdraw
                print(f"Your new balance is ${balance}")

        elif menu == 3:
            print(f"Your balance is ${balance}")

        elif menu == 4:
            print("Thank you for using our services!")
            break  # Exit the loop

        else:
            print("Please choose a number from 1 to 4 only.")

    else:
        print("Invalid input. Please type a number from 1 to 4.")
