"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 6
tries = 0
# DONE: select target word at random from TARGET_WORDS
target_word = random.choice(open(TARGET_WORDS).read().split())
# print("the target word is: " + target_word)

print("Welcome to my simple wordle clone. Try to find the 5-letter word in 6 guesses or less.")
print("2 = right letter, right place, 1 = right letter, wrong place, 0 = not in word")
# DONE: repeat for MAX_TRIES valid attempts
# (start loop)
while tries < MAX_TRIES:
    guess = input("Enter guess? ")
    if guess in open(VALID_WORDS).read().split():
        print("Your guess is a valid guess")
        tries += 1

    else:
        print("Invalid guess, please try a real 5 letter word")
        tries += 0
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

    for letter in guess:
        guess_list.append(letter)
    print("guess:  " + str(guess_list))

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
            score_list.append("2")
        elif value in target_list:
            score_list.append("1")
        else:
            score_list.append("0")
    print("Score:  " + str(score_list))

    # For later, find a way to have: 🟩🟧🟥 as options for scoring without messing up the alignment

    if guess == target_word:
        print("Your guess is correct!")
        tries = 6

    elif guess != target_word:
        print("Your guess is wrong!")

# (end loop)
print("Game Over")


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
