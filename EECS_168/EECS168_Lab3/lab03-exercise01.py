'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/09/2024
Lab: lab03
Last modified: 02/12/2024
Purpose: Sequence Search
'''
word = input('Enter a string: ')
case = input('Do you want case-sensitive match?: ')
if case == 'y' or case == 'Y':
    sequence = input('Enter a sequence to count: ')
    amount = word.count( sequence )
    print('In the string', word, 'the sequence', sequence, 'occurs', amount, 'time(s)')
else:
    sequence = input('Enter a sequence to count: ')
    lowercase_word = word.lower()
    lowercase_sequence = sequence.lower()
    amount = lowercase_word.count( lowercase_sequence )
    print('In the string', word, 'the sequence', sequence, 'occurs', amount, 'time(s)')
