# HANGMAN 4 --- Keeping track of the lives

import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6


# Testing code
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

    # looping through each position in the chosen_word 
    # if the letter matches guess at that position, then the guess should 
    # displayed removing the blank at that position

    for position in range(word_len):
        # if chosen_word[position] == guess:
        #     display[position] = guess. OR
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # for guess not in letter, the lives get reduced
    if guess not in chosen_word:
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
