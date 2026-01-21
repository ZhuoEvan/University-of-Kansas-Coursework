'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/25/2024
Lab: lab03
Last modified: 9/28/2024
Purpose: Browser History Command Control
'''
#command.py

#Importing Browser Class
from browser import Browser

class Command:
    #Initial Variables
    def __init__(self, command):
        self._command = command
        self.browser = Browser()

    #Running the Browser Program
    def run(self):
        with open(self._command, 'r') as command_list:
            total_command = self.command_open(command_list)
            #Commiting the Four Command Types
            for action in total_command:
                #Navigate Command
                if action[0].upper() == 'NAVIGATE':
                    url = action[1]
                    self.browser.navigate_to(url)
                #Forward Command
                elif action[0].upper() == 'FORWARD':
                    self.browser.forward()
                #Back Command
                elif action[0].upper() == 'BACK':
                    self.browser.back()
                #History Command
                elif action[0].upper() == 'HISTORY':
                    self.browser.history()
                #Error Check: Invalid Command
                else:
                    raise RuntimeError('Invalid Command')

    #Opening and Converting Command File to be Readable
    def command_open(self, command_list):
        unsplit_command = []
        split_command = []
        for index in command_list:
            command = index.strip()
            unsplit_command.append(command)
        for command in unsplit_command:
            clean_command = command.split(' ')
            split_command.append(clean_command)
        return split_command
