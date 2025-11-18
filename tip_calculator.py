print("====== TIP CALCULATOR APP ======")

bill = float(input("What is your bill in Kshs? "))
tip_percentage = float(input("What percentage of the bill do you want to give as tip? "))
actual_tip = (tip_percentage/100)*bill
total_amount = bill+actual_tip
print(f"Dear customer, your total bill is {bill + actual_tip}")