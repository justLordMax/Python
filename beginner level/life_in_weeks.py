# life in weeks

# collect user age 
age = int(input("what is your current age? "))

# getting the actual remaining age
definite_age = 90
remaining_age = definite_age - age

# getting the age in days, weeks and months to reach 90years
age_in_days = remaining_age * 365
age_in_weeks = remaining_age * 52
age_in_months = remaining_age * 12

# the result
message = f"You have {age_in_days} days, {age_in_weeks} weeks and {age_in_months} months left." 
print(message)
