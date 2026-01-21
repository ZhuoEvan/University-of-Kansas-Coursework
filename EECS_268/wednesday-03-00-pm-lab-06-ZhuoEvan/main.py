'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/28/2024
Lab: lab06
Last modified: 11/04/2024
Purpose: Binary Search Tree Main
'''
#main.py

from binarytree import BinaryTree

#User Menu
def main():
    #Global Variables
    logout = 0
    my_binary_tree = BinaryTree()

    #Program is running condition
    while logout == 0:
        print(menu())
        user_choice = input('Select an Option: ')
        
        #Add to the Binary Search Tree
        if user_choice == '1' or user_choice.lower() == 'add':
            try:
                my_binary_tree.run('add')
            except:
                print('Program has encountered an invalid input error')
        
        #Print the Binary Search Tree
        elif user_choice == '2' or user_choice.lower() == 'print':
            my_binary_tree.run('print')

        #Reset the Binary Search Tree (Extra Function)
        elif user_choice == '3' or user_choice.lower() == 'reset':
            my_binary_tree.run('reset')
            
        #Quit the Program
        elif user_choice == '4' or user_choice.lower() == 'quit':
            logout = 1
        #Error Check: Valid Input
        else:
            print(f'The input [{user_choice}] is invalid.\n')
    print('Exiting the Program...')
    input('Enter Key to Exit')

#Generic Menu Design
def menu():
    output = '===== Menu =====\n'
    output += '1) Add\n'
    output += '2) Print\n'
    output += '3) Reset\n'
    output += '4) Quit\n'
    output += '================\n'
    return output

main()
