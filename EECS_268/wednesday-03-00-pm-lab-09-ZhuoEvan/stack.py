'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Stack Class
'''
#stack.py

#Importing Node Class
from node import Node

class Stack:
    #Initializing Stack Class
    def __init__(self):
        self._top = None

    #Push Function
    def push(self, entry):
        #First Node Scenario
        if self.is_empty():
            self._top = Node(entry)
        #Push Previous Top into Next and Set Entry as Top
        else:
            previous_node = self._top
            self._top = Node(entry)
            self._top.next = previous_node

    #Pop Function
    def pop(self):
        #Error Check: Empty Stack
        if self.is_empty():
            raise RuntimeError('Stack Empty')
        #Set Next as Top and Return Previous Top
        else:
            pop_value = self._top
            next_value = self._top.next
            self._top = next_value
            return pop_value

    #Peek Function
    def peek(self):
        #Error Check: Empty Stack
        if self.is_empty():
            raise RuntimeError('Stack Empty')
        #Return Stack Top
        else:
            return self._top

    #Is_Empty Function
    def is_empty(self):
        return self._top is None

    #String Operator
    def __str__(self):
        output = f'{self._top}'
        return output

    #Representation Operator
    def __repr__(self):
        output = f'{self._top}'
        return output
    