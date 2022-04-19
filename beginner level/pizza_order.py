# Pizza order program
print("Welcome to python Pizza Deliveries!")

size = input("What size of pizza do you want? S, M, L?  ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_s = 2
pepperoni_ml = 3

cheese = 1
bill = 0

if size == "S":
    bill += 15
    # print("You pay $15 for small pizza")
    if add_pepperoni == "Y":
        bill += 2
        # print("Pepperoni for small pizza added")
    elif add_pepperoni == "N":
        bill += 0
        
elif size == "M":
    bill += 20
    # print("You pay $20 for medium pizza")
    if add_pepperoni == "Y":
        bill += 3
        # print("Pepperoni for medium pizza added")
    elif add_pepperoni == "N":
        bill += 0

elif size == "L":
    bill += 25
    # print("You pay $25 for large pizza")
    if add_pepperoni == "Y":
        bill += 3
        # print("Pepperoni for large pizza added")
    elif add_pepperoni == "N":
        bill += 0

if extra_cheese == "Y":
    bill += cheese

# total bill
print(f"Your final bill is {bill}")