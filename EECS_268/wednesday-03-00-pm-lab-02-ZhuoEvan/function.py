'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/23/2024
Lab: lab02
Last modified: 9/25/2024
Purpose: Function Class
'''
#function.py

class Function:
    #Initial Variables
    def __init__(self, name, exception):
        self._name = name
        self.exception = exception

    #String of a Function
    def __str__(self):
        output = f'{self._name}, {self.exception}'
        return output

    #Representation of a Function
    def __repr__(self):
        output = f'{self._name}, {self.exception}'
        return output
