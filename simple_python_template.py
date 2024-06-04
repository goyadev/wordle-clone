"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 6
tries = 0
tries_count = 0
# DONE: select target word at random from TARGET_WORDS
# target_word = random.choice(open(TARGET_WORDS).read().split())
with open(TARGET_WORDS) as file:
    target_word_list = file.read()
target_word_list = target_word_list.split()
target_word = random.choice(target_word_list)

with open(VALID_WORDS) as file:
    valid_word_list = file.read()
valid_word_list = valid_word_list.split()

# [helper for debugging, uncomment below, so you can see the word]
# print("For testing, the target word is: " + target_word)
print('✌⊂(✰‿✰)つ✌')
print("Welcome to my simple wordle clone.\nTry to guess the 5-letter word in 6 guesses or less.")
print("\n- ? = right letter, wrong place\n- / = not in word\n")

player_name = input("Enter your player name\n(Want to be anonymous? Press 'enter'):")
if player_name == '' or player_name == ' ':
    player_name = random.choice(valid_word_list) + "-player"
print("Hello " + player_name + "\n")
# DONE: repeat for MAX_TRIES valid attempts
# (start loop)
while tries < MAX_TRIES:
    guess = input("Enter guess? ")
    guess_lower = guess.lower()
    if guess_lower in valid_word_list:
        print("Your guess is a valid guess")
        tries += 1
        tries_count += 1

    else:
        print("Invalid guess, please try a real 5 letter word")
        continue
    print("Number of tries: " + str(tries) + "/" + str(MAX_TRIES))

# DONE: ensure guess in VALID_WORDS as above
#     if guess in (open(VALID_WORDS).read(), target_word):
#         print("Your guess is a valid guess")

# DONE: provide clues for each character in the guess using your scoring algorithm
    guess_list = []
    target_list = []
    clue_list = []
    score_list = []

    for letter in target_word:
        target_list.append(letter)
    # print("target: " + str(target_list))

    for letter in guess_lower:
        guess_list.append(letter)
    # print("guess:  " + str(guess_list))

    # # This gives many hints to the player. It was a first try at scoring
    # for element in target_list:
    #     if element in guess_list:
    #         clue_list.append(element)
    #     else:
    #         clue_list.append(" ")
    # print("clue:   " + str(clue_list))

    guess_list_tuple = list(enumerate(guess_list))
    # print(guess_list_tuple)

    target_list_tuple = list(enumerate(target_list))
    # print(target_list_tuple)

    for key, value in guess_list_tuple:
        if value in target_list_tuple[key]:
            score_list.append(value)
        elif value in target_list:
            score_list.append("?")
        else:
            score_list.append("/")
    # print("Score:  " + str(score_list))

    guess_clue = ''
    for element in guess_list:
        guess_clue += str(element).upper() + " "
    print("GUESS: " + guess_clue)

    score_clue = ''
    for element in score_list:
        score_clue += str(element).upper() + " "
    print("SCORE: " + score_clue)

    # For later, find a way to have: 🟩🟧🟥 as options for scoring without messing up the alignment
    success_statement = ''
    if guess_lower == target_word:
        print('٩(^‿^)۶')
        print("Your guess is correct!\n")
        tries = 6
        success_statement = 'Successful'

    elif guess_lower != target_word:
        print('(✖╭╮✖)')
        print("Your guess is wrong!\n")
        success_statement = 'Unsuccessful'

# (end loop)

save_file = 'scores.txt'

with open(save_file, 'a') as file:
    file.write(player_name + ', Word:' + target_word + ", Tries:" + str(tries_count) + ', ' + success_statement + '\n')


print("Game Over")
print("The word was " + target_word)


# NOTES:
# ======
# - Add your own flair to the project
# - You will be required to add and refine features based on changing requirements
# - Ensure your code passes any tests you have defined for it.

# SNIPPETS
# ========
# A set of helpful snippets that may help you meet the project requirements.

# def pick_target_word(words=None):
#     """returns a random item from the list"""
#     words = ['a', 'b', 'c']
#     return random.choice(words)
#
#
# def display_matching_characters(guess='hello', target_word='world'):
#     """Get characters in guess that correspond to characters in the target_word"""
#     i = 0
#     for char in guess:
#         print(char, target_word[i])
#         i += 1

# Uncomment to run:
# display_matching_characters()
# print(pick_target_word())
