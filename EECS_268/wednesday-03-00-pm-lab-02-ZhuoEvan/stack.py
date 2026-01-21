'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/23/2024
Lab: lab02
Last modified: 9/25/2024
Purpose: Stack Class
'''
#stack.py

#Importing Node Class
from node import Node

class Stack:
    #Initializing Stack Class
    def __init__(self):
        self._top = None

    #Push Old Top into Next and Set Top as Entry
    def push(self, entry):
        self._next = self._top
        self._top = entry

    #Set Next as Top and Returning Old Top
    def pop(self):
        #Error Check: Empty Stack
        if self.is_empty():
            raise RuntimeError('Stack Empty')
        else:
            pop_value = self._top
            self._top = self._next
            return pop_value

    #Return Top
    def peek(self):
        #Error Check: Empty Stack
        if self.is_empty():
            raise RuntimeError('Stack Empty')
        else:
            return self._top

    #Check Top
    def is_empty(self):
        return self._top is None

    #String of a Stack 
    def __str__(self):
        output = f'{self._top}'
        return output

    #Representation of a Stack
    def __repr__(self):
        output = f'{self._top}'
        return output
    
