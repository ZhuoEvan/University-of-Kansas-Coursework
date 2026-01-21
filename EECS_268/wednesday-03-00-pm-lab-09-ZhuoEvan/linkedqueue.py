'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: LinkedQueue Class
'''
#linkedqueue.py

#Importing Node Class
from node import Node

class LinkedQueue:
    #Initializing LinkedQueue Class
    def __init__(self):
        self._front = None
        self._back = None

    #Enqueue Function
    def enqueue(self, entry):
        entry_node = Node(entry)
        #First Node Scenario
        if self.is_empty():
            self._front = entry_node
            self._back = entry_node
        #Other Nodes Scenario
        else:
            previous_node = self._back
            self._back = entry_node
            self._back.next = previous_node

    #Dequeue Function
    def dequeue(self):
        #Error Check: Empty Queue
        if self.is_empty():
            raise RuntimeError('Queue Empty')
        else:
            #Storing the self._front value into exit_node
            exit_node = self._front
            #Only one node inside the linkedqueue scenario
            if self._front == self._back:
                self._front = None
                self._back = None
                return exit_node
            #Two or more nodes inside the linkedqueue scenario
            move_node = self._back
            gate = 0
            #Loop that moves the move_node starting from self._back
            #until it reaches the node before the self._front node
            while gate != 1:
                if move_node.next != self._front:
                    move_node = move_node.next
                else:
                    gate = 1
            #Setting the new self._front and returning
            #the previous self._front
            self._front = move_node
            return exit_node

    #Peek Function
    def peek(self):
        #Error Check: Empty Queue
        if self.is_empty():
            raise RuntimeError('Queue Empty')
        #Return Front
        else:
            return self._front

    #Is_Empty Function
    def is_empty(self):
        return self._front is None

    #String Operator
    def __str__(self):
        output = f'{self._front}'
        return output

    #Representation Operator
    def __repr__(self):
        output = f'{self._front}'
        return output