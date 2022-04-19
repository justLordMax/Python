# HANGMAN Step 1

# import the random module
import random

word_list = ["ardvark", "baboon", "camel"]

# choosen_word = []
# randomly choosing a word from the word_list
choosen_word = list(random.choice(word_list))

# or
# choosen_word = random.choice(word_list)

# Asking the user to guess a letter in lower case then,
# assigning it to a variable guess
guess = input("Guess a letter: ").lower()

# checking if the letter guessed by the user is one of
# the letter in the choosen_word
for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")