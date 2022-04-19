# HANGMAN 5 --- Final change

import random 
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

# OR word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

lives = 6

# OR stages = hangman_art.stages

# OR logo = hangman_art.logo
print(logo)

# Testing code -- HINT
print(f"pssst, the word is {chosen_word}")

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

    # feedback on the letter already guessed
    if guess in display:
        print(f"You've already guessed the letter {guess}")

    # looping through each position in the chosen_word 
    # if the letter matches guess at that position, then the guess should 
    # displayed removing the blank at that position

    # check guessed letter`
    for position in range(word_len):
        # if chosen_word[position] == guess:
        #     display[position] = guess. OR
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # for guess not in letter, the lives get reduced
    if guess not in chosen_word:
        print(f"You guessed {guess}, which is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
    # joining all the elements in the list and turn it to a string
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])
