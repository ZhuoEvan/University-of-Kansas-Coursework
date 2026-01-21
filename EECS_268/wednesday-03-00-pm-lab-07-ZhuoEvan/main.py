'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/05/2024
Lab: lab07
Last modified: 11/13/2024
Purpose: Binary Search Tree Two Main
'''
#main.py

from controlcenter import ControlCenter
from pokemon import Pokemon

#Title Card Function
def title_card():
    title = '================\nInput file name with dot extension\n================'
    return title

#Opening a File
def open_file(file_name):
    with open(file_name, 'r') as poke_file:
        pokedex = []
        for entry in poke_file:
            #Cleaning and Spliting the Line
            entry_line = entry.strip().split('\t')

            #Error Check: Valid Input
            if len(entry_line) != 3:
                raise RuntimeError
            else:
                #Converting Line Data into Pokemon Class Element
                my_pokemon = Pokemon(entry_line[0], int(entry_line[1]), entry_line[2])
                pokedex.append(my_pokemon)
    return pokedex

#Receive Input File from User
def main():
    #Initial Variables
    gate = 0

    #Valid Input While Loop
    while gate != 1:
        try:
            print(title_card())
            user_file = input('File Name: ')
            #user_file = 'pokemon.txt' #Forced Testing
            my_file = open_file(user_file)
            gate = 1

        except:
            print('An Exception has been Raised')
    
    #Proceed with the Process
    my_control = ControlCenter(my_file)
    my_control.run()

main()