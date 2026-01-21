'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/13/2024
Lab: lab08
Last modified: 11/18/2024
Purpose: Hospital Program Functions
'''
#controlcenter.py

from patient import Patient
from maxheap import MaxHeap

class ControlCenter:
    def __init__(self, command_list):
        #Initial Variables
        self._command_list = command_list
        self._hospital = MaxHeap()
        self._arrival_order = 0
    
    #Count Function
    def _count(self):
        #Initial Variables
        cur_count = len(self._hospital._heap)
        #Print the Number of Patients Waiting
        if cur_count == 0:
            print('There are no patients waiting.\n')
        elif cur_count == 1:
            print(f'There are {cur_count} patient waiting.\n')
        elif cur_count > 1:
            print(f'There are {cur_count} patients waiting.\n')
        #Error Check: Negative Integer
        else:
            raise RuntimeError('Negative Patients?!')

    #Treat Function
    def _treat(self):
        #No Patient Present Scenario
        if len(self._hospital._heap) == 0:
            print('Congrats on Treating Actual Air!\n')
        #Run the Program Normally
        else:
            self._hospital.remove()

    #Next Function
    def _next(self):
        #No Patient Present Scenario
        if len(self._hospital._heap) == 0:
            print('Next patient:\n\tNo Patient Present\n')
        #Run the Program Normally
        else:
            print(f'Next patient:\n{self._hospital._heap[0]}\n')

    #Arrive Function
    def _arrive(self, line):
        #Log Patient Details into a Patient Class
        my_patient = Patient(line[1], line[2], int(line[3]), line[4], int(line[5]), self._arrival_order)
        #Add Patient to MaxHeap
        self._hospital.add(my_patient)
    
    #Run the Hospital Program
    def run(self):
        #Initial Variables
        error_log = 0
        print('[Hospital Program Run]\n')
        try:
            #Proceed through all Commands in Input File
            for command in self._command_list:
                #Arrive Function
                if command[0].upper() == 'ARRIVE':
                    #Error Check: Valid Input
                    if len(command) == 6:
                        self._arrival_order += 1
                        self._arrive(command)
                    else:
                        error_log += 1
                        print(f'[Hospital Program has Encountered an Error! ({error_log}/3)]\n')
                        if error_log >= 3:
                            raise RuntimeError('ARRIVE Command is Incomplete!')
                    
                #Next Function
                elif command[0].upper() == 'NEXT':
                    self._next()

                #Treat Function
                elif command[0].upper() == 'TREAT':
                    self._treat()

                #Count Function
                elif command[0].upper() == 'COUNT':
                    self._count()

                #Error Check: Valid Command
                else:
                    error_log += 1
                    print(f'[Hospital Program has Encountered an Error! ({error_log}/3)]\n')
                    if error_log >= 3:
                        raise RuntimeError('Unreadable Command')
        
        #Multiple Errors: Force Shut Down the Hospital Program
        except:
            print('[Hospital Program has encountered multiple ERROR.]')
            print('[Please Fix the ERROR then run the Hospital Program.]\n')
