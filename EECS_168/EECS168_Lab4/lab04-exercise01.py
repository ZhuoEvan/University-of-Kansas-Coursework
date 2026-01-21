'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/13/2024
Lab: lab04
Last modified: 02/18/2024
Purpose: Going to the Grocery Store
'''
print('Welcome to your Shopping List!')
print('1) Add item')
print('2) Check off item')
print('3) Print list')
print('4) Exit')
choice = int(input('Enter a choice: '))
grocery = []
while choice != 4:
    if choice == 1:
        addition = str(input('What will you add to the list?: '))
        grocery.append(addition)
        print()
        print('Welcome to your Shopping List!')
        print('1) Add item')
        print('2) Check off item')
        print('3) Print list')
        print('4) Exit')
        choice = int(input('Enter a choice: '))
    elif choice == 2:
        check = int(input('Which item will you check off?: '))
        strike = grocery[check - 1]
        front_strike = strike[0]
        back_strike = strike[len(strike) - 1]
        strike_word = ''
        for letter in range(1, len(strike) - 1):
            strike_word = strike_word + '-'
        strike_word = front_strike + strike_word + back_strike
        grocery.pop(check - 1)
        grocery.insert(check - 1, strike_word)
        print()
        print('Welcome to your Shopping List!')
        print('1) Add item')
        print('2) Check off item')
        print('3) Print list')
        print('4) Exit')
        choice = int(input('Enter a choice: '))
    elif choice == 3:
        print('Here is your list:')
        for word in grocery:
            print(grocery.index(word) + 1,')', word) 
        print()
        print('Welcome to your Shopping List!')
        print('1) Add item')
        print('2) Check off item')
        print('3) Print list')
        print('4) Exit')
        choice = int(input('Enter a choice: '))
    else:
        print('Invalid input')
        choice = 4
if choice == 4:
    print('Goodbye!')
