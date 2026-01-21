'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/23/2024
Lab: lab02
Last modified: 9/25/2024
Purpose: Process Class
'''
#process.py

from stack import Stack
from function import Function

class Process:
    #Initial Variables
    def __init__ (self, name):
        self._name = name
        self.call_stack = Stack()

    #Creating the Function
    def process_function(self, function, exception):
        self._function = function
        self._exception = exception
        my_func = Function(self._function, self._exception)
        return my_func

    #Pushing the function into the Stack
    def func_stack(self, function):
        self._function = function
        self.call_stack.push(self._function)

    #Checking for functions inside the stack
    def func_checker(self):
        if self.call_stack.is_empty():
            return True

    #String of a Process
    def __str__(self):
        output = f'{self._name}'
        return output

    #Representation of a Process
    def __repr__(self):
        output = f'{self._name}'
        return output
