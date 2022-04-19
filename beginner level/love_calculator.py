# Love Calculator
print("WELCOME TO THE LOVE CALCULATOR!")

name = input("What is your name? \n")
partners_name = input("What is their name? \n")

# convert the names to lower case
lower_name = name.lower()
lower_partners_name = partners_name.lower()

# getting the number of true love
t = lower_name.count("t") + lower_partners_name.count("t")
r = lower_name.count("r") + lower_partners_name.count("r")
u = lower_name.count("u") + lower_partners_name.count("u")
e = lower_name.count("e") + lower_partners_name.count("e")
true_total = t + r + u + e

l = lower_name.count("l") + lower_partners_name.count("l")
o = lower_name.count("o") + lower_partners_name.count("o")
v = lower_name.count("v") + lower_partners_name.count("v")
love_total = l + o + v + e

score = int(f"{true_total}{love_total}")

# condition for compatibility
if score < 10 and score > 90:
    print(f"Your score is {score}%, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}%, you are alright together")
else:
    print(f"Your score is {score}%")
    