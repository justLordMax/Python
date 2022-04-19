# Tip Calculator
message = "Welcome to the tip calculator"
print(message)

# User input  bill 
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

percentage_tip = 1 + (tip / 100)
bill_with_tip = total_bill * percentage_tip
split = int(input("How many people to split the bill? "))

individual_pay = round(bill_with_tip / split, 2)
print(f"Each person should pay: ${individual_pay}")
