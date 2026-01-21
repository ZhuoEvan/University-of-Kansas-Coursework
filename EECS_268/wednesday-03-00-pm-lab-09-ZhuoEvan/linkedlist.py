'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: LinkedList Class
'''
#linkedlist.py

#Importing Node Class
from node import Node

class LinkedList:
    #Initial Variables
    def __init__(self):
        self._front = None
        self._length = 0

    #Return the Current Length
    def length(self):
        return self._length

    #Inserting Entry at an Index (No Node is Removed)
    def insert(self, index, entry):
        entry_node = Node(entry)
        #Error Check: Within Linked List Bounds
        if index > self._length:
            raise RuntimeError('Not in Linked List')
        #New LinkedList Scenario
        elif self._front is None:
            self._front = entry_node
            self._length += 1
        else:
            jumper = self._front
            for _ in range(0, index - 1):
                jumper = jumper.next              
            previous_node = jumper 
            previous_node.next = entry_node
            #Reset Jumper
            jumper = self._front
            for _ in range(0, index):
                jumper = jumper.next
            #Node that will be Replaced by Entry
            current_node = jumper
            following_node = current_node.next
            entry_node.next = following_node
            self._length += 1

    #Get_Entry Function
    def get_entry(self, index):
        jumper = self._front
        #Error Check: Within LinkedList Bounds
        if index > self._length:
            raise IndexError('Not in Linked List')
        else:
            for _ in range(0, index):
                jumper = jumper.next
            #Return the Node at Index
            return jumper

    #Setting an Entry as Index Node (Length Stays the Same) [Unused]
    def set_entry(self, index, entry):
        entry_node = Node(entry)
        #Error Check: Within LinkedList Bounds
        if index > self._length:
            raise IndexError('Not in LinkedList')
        else:
            jumper = self._front
            for _ in range(0, index):
                jumper = jumper.next
            #Replace the node.entry as entry
            jumper.entry = entry

    #Remove Node at the Specified Index
    def remove(self, index):
        #Error Check: LinkedList Exist
        if self._length == 0:
            raise RuntimeError('Not in Linked List')
        else:
            #Accessing Node that will be Removed
            jumper = self._front
            for _ in range(0, index):
                jumper = jumper.next
            removed_node = jumper
            #Reset Jumper
            jumper = self._front
            for _ in range(0, index - 1):
                jumper = jumper.next
            previous_node = jumper
            previous_node.next = removed_node.next
            self._length -= 1
            return removed_node
            
    #Resets the LinkedList to Initial Values
    def clear(self):
        self._front = None
        self._length = 0