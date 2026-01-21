'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/25/2024
Lab: lab03
Last modified: 9/28/2024
Purpose: Browser History Start
'''
#start.py

#Importing Command Class
from command import Command

def main():
    #Receiving the Command File from User
    command_list = input('Enter the command file name: ')
    my_browser = Command(command_list)
    my_browser.run()

if __name__ == "__main__":
    main()
