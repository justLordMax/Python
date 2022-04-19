# SPECIFIED NUMBER --- METHOD 1

# secrete_number = 9
# guess_limit = 3
# current_guess = 0

# while current_guess != guess_limit:
#     guess = int(input("Guess: "))
#     current_guess += 1
    
#     if guess == secrete_number:
#         print("You Win!")
#         break
# else:
#     print("You Failed!")


# NUMBER AT RANDOM --- METHOD 1

import random
secrete_number = random.randint(1, 9)
guess_limit = 3
current_guess = 0

while current_guess != guess_limit:
    guess = int(input("Guess: "))
    current_guess += 1
    
    if guess == secrete_number:
        print("You Win!")
        break
else:
    print("You Failed!")
    

