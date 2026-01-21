'''
Author: Evan Zhuo
KUID: 3109819
Date: 03/19/2024
Lab: lab07
Last modified: 03/25/2024
Purpose: Dictionary Input
'''
#Variables
symbol = ['!', '?', ':', ';', ',', '|', '.', '[', ']', '(', ')', '--']
#Functions
def build_count(text):
    word_dict = {}
    clean_line = []
    delimiter = ' '
    for line in text:
        line = line.lower()
        line = line.split(delimiter)
        for word in line:
            key = clean_word(word)
            clean_line.append(key)
            key_value = clean_line.count(key)
            word_dict[key] = key_value
    word_dict.pop('')
    return word_dict
    
def clean_word(word):
    for character in symbol:
        word = word.strip()
        clean_word = word.strip(character)
        word = word.replace(word, clean_word)
        ans = clean_word
    return ans

def unique_words(word_counts):
    unique_list = []
    for key, value in word_counts.items():
        if value == 1:
            unique_list.append(key)
    return unique_list
    
def main():
    greeting = 'Welcome to the word counter!'
    print(greeting.center(50, '='))
    file = input('Enter a file name: ')
    input_file = open(file, 'r')
    word_dict = build_count(input_file)
    unique_dict = unique_words(word_dict)
    print('The file', file, 'has been processed.')
#word_count.txt
    word_file = open('word_count.txt', 'w')
    for key, value in word_dict.items():
        word_file.write(f'{key} : {value}')
        word_file.write('\n')
    word_file.close()
#unique_file.txt
    unique_file = open('unique_words.txt', 'w')
    for word in unique_dict:
        unique_file.write(word)
        unique_file.write('\n')
    unique_file.close()
    print('Output stored in word_count.txt and unique_words.txt')
    print('Exiting...')
    
main()
