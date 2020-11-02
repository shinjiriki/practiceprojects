# Hangman
# This will be similar to guessing the number, except we are guessing the word. The user needs to guess letters,
# Give the user no more than 6 attempts for guessing wrong letter. This will mean you will have to have a counter.
# You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a random word to use.

import random

# global variable later
i = 0 
j = 0
k = 0
string = ''
symbols = " '&.-"

# Picking Category
print('Category :')
print('1. Fruits')
print('2. Countries')
print('3. Famous Company')
while True:
    choices = input('Please pick a category : ')
    if choices == '1':
        directory = 'Dictionary/fruits.txt'
        break
    elif choices == '2':
        directory = 'Dictionary/countries.txt'
        break
    elif choices == '3':
        directory = 'Dictionary/company.txt'
        break
    else:
        print('Please input choices')

# Pick the word
filename = open(directory)
word = filename.readlines()  # read all the lines in file
count = len(word)
wordpos = random.randint(0, count-1)  # pick a word randomly based on its position
guessword = word[wordpos].rstrip().lower()  # get the word, rstrip() to make sure the "/n" won't be count
wordlen = len(guessword)
guessword = list(guessword)  # turning the word into a list of characters
matched_indexes = []

# Guess the word
while i < wordlen:
    matched_indexes.append('_')
    for sym in symbols:
        if sym == guessword[i]:
            matched_indexes[i] = guessword[i]
    i += 1

print(matched_indexes)

# Player
lives = 6
used = []  # usedwords
while lives > 0:
    # End the game when no more _
    if '_' not in matched_indexes:
        for k in matched_indexes:
            string += k
        print(f'Congratulations! The word is {string}')
        break

    print(f'\nYour current lives is {lives}')
    player = input('Input a character : ')[0]  # to get only 1 character

    if player in guessword:
        print(f'{player} is present')
        while j < wordlen:
            if player == guessword[j]:
                matched_indexes[j] = player
            j += 1
        j = 0
        print(matched_indexes)
    else:
        print(f'{player} is not present')
        used.append(player)  # appending all of the characters that has been used
        print(f'Used words : {used}')
        lives = lives - 1
        print(matched_indexes)

# Gameover
if lives == 0:
    for k in guessword:
        string += k
    print('Game Over')
    print(f'The word is {string}')
