# Improved BMI calculator
from decimal import ROUND_UP


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

# conditions
if bmi < 18.5:
    print(f"You BMI is {bmi}, you are Underweight")
elif bmi < 25:
    print(f"You BMI is {bmi}, you are Normal weight:")
elif bmi < 30:
    print(f"You BMI is {bmi}, you are Overweight")
elif bmi < 35:
    print(f"You BMI is {bmi}, you are Obese")
else:
    print(f"You BMI is {bmi}, you are Clinically obese")

