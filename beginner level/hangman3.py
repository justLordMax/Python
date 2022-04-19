# HANGMAN STEP 3 --- Repeatition

# import the random module
import random


# create a word list and select a word
# at random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
# print(f"pssst, the word is {chosen_word}")

# create empty list called display
display = []

# replace each letter in chosen_word with a blank 
# inserted into the display list
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
# print(display)

# user to guess a letter

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # looping through each position in the chosen_word 
    # if the letter matches guess at that position, then the guess should 
    # displayed removing the blank at that position

    for position in range(word_len):
        # if chosen_word[position] == guess:
        #     display[position] = guess. OR
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")


