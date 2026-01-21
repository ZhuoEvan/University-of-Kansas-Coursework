'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/23/2024
Lab: lab02
Last modified: 9/25/2024
Purpose: CPU Scheduler
'''
#cpu_scheduler.py

from linkedqueue import LinkedQueue
from process import Process

class CPU_Scheduler:
    #Initial Variables
    def __init__(self, command_list):
        self._command_list = command_list
        
    def run(self):
        #Converting file into Command Lines
        command_center = self.command_control()
        #Setting up the CPU Scheduler Queue
        cpu_scheduler = LinkedQueue()
        process_list = []
        index = 0
        #Command Seperated Options
        #Error Check: Valid Command Inputs
        for command in command_center:
            #START function
            if command[0].upper() == 'START':
                #Creating a Process with main in Stack
                process_name = command[1]
                process = self.process_creation(process_name)
                process_list.append(process)
                cpu_scheduler.enqueue(process)
                print(f'{process_name} added to queue')
                
            #CALL function
            elif command[0].upper() == 'CALL':
                #Error Check: Empty Queue
                cpu_scheduler.is_empty()
                #Assigning variables for process
                current_process = cpu_scheduler.dequeue()
                current_process_data = process_list[index]
                function = command[1]
                exception = command[2]
                if exception.lower() == 'yes':
                    self.raise_function(current_process_data)
                else:
                    print(f'{current_process} calls {function}')
                    cpu_scheduler.enqueue(current_process)
                    process_list.append(current_process_data)
                    index += 1

            #RETURN function
            elif command[0].upper() == 'RETURN':
                current_process = cpu_scheduler.dequeue()
                current_process_data = process_list[index]
                print(f'{current_process} returns from main')
                if current_process_data.func_checker() is True:
                    self.raise_function(current_process_data)
                else:
                    cpu_scheduler.enqueue(current_process)
                    process_list.append(current_process_data)
                    index += 1
                
            #RAISE function
            elif command[0].upper() == 'RAISE':
                current_process = cpu_scheduler.dequeue()
                print(f'{current_process} process has ended')
                index += 1
                
            else:
                raise RuntimeError('Invalid Command')

    #Opening the Command File
    def command_control(self):
        command_list = []
        all_command_list = []
        with open(self._command_list, 'r') as command:
            for line in command:
                clean_line = line.strip()
                command_list.append(clean_line)
            for line in command_list:
                single_command = line.split(' ')
                all_command_list.append(single_command)
        return all_command_list

    #Creates the process
    def process_creation(self, process_name):
        process = Process(process_name)
        return process

    #Raise function
    def raise_function(self, data):
        if data.func_checker() is True:
            print(f'{data} process has ended')
        else:
            return True
            
            
        
        
        
        
        
        
        

