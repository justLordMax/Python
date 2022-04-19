# Treasure Island

print("WELCOME TO TREASURE ISLAND!")
message = "Your mission is to find the lost treasure"
print(message)

warning = "WARNING: Type the words in quote \n"
print(warning)

# 
# 

first_step = input("Your're at an hill top. Where do you want to go? Type 'left' or 'right': ").lower()
if first_step == "left":
    second_step = input("\nYou just arrived at the river. There is an Island in the middle of the river. Do you want to 'swim' or 'wait' for a boat: ").lower()
    if second_step == "wait":
        third_step = input("\nYou have arrived at the door to recover the lost treasure, what door color is it? 'red', 'yellow' or 'blue': ").lower()
        if third_step == "yellow":
            print("\nCongratulations! You have found the lost treasure. Weldone")
        else:
            print("\nOops, Game Over! You got eaten by the dragon guidian")
    else:
        print("\nGame Over! You got eaten by a Crocodile")

else:
    print("\nGame Over! You fell into the Lions cave")
