'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/13/2024
Lab: lab08
Last modified: 11/18/2024
Purpose: Hospital Program Main
'''
#main.py

from controlcenter import ControlCenter

#Basic Open File Function
def open_file(file):
    #Initial Variables
    open_file = []

    #Open User File
    with open(file, 'r') as read_file:
        for line in read_file:
            #Remove NewLines and Split ARRIVE Information
            open_file.append(line.strip().split(' '))
    #Return a List in List
    return open_file

#Basic Menu Function
def menu():
    menu = '========================================\n'
    menu += 'Input the File Name with dot extension\n'
    menu += '========================================'
    return menu

#Main Function
def main():
    #Initial Variables
    input_gate = 0

    #Getting User File
    while input_gate == 0:
        try:
            print(menu())
            user_file = input('File Name: ')
            read_file = open_file(user_file)
            print('[Valid File Input]')
            input_gate = 1
        except:
            print('[Invalid File Input]\n')
    
    #Passing Control to controlcenter.py
    print('[Proceeding to Next Step...]\n')
    my_control = ControlCenter(read_file)
    my_control.run()

    #Program Complete Statement
    print('[Hospital Program has been Completed]')

main()