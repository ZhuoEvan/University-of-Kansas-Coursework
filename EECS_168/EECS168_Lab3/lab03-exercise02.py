'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/09/2024
Lab: lab03
Last modified: 02/12/2024
Purpose: Secret Word Guess
'''
print('Guess the secret phrase!')
word = 'BRINGCOFFEE'
attempt = 1
guess = input('Guess: ')
upper_guess = guess.upper()
while upper_guess != 'BRINGCOFFEE':
    if len(upper_guess) < len(word):
        attempt = attempt + 1
        print('Too few characters')
        guess = input('Guess: ')
        upper_guess = guess.upper()
    elif len(upper_guess) > len(word):
        attempt = attempt + 1
        print('Too many characters')
        guess = input('Guess: ')
        upper_guess = guess.upper()
    elif len(upper_guess) == len(word):
        attempt = attempt + 1
        letter = 0
        for index in range(0, len(word)):
            if upper_guess[index].count(word[index])== 1:
                letter = letter + 1
        print('Correct letters:', letter)
        guess = input('Guess: ')
        upper_guess = guess.upper()
if upper_guess == 'BRINGCOFFEE':
    print('Correct!')
    print('Number of guesses:', attempt)
