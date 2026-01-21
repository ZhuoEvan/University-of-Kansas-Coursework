'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Operation Function
'''
#operationtimer.py

#Import Modules
import random
from stack import Stack
from linkedqueue import LinkedQueue
from linkedlist import LinkedList
from maxheap import MaxHeap
from binarytree import BinaryTree
import sys

#Increase Recursion Limit
sys.setrecursionlimit(100000)

class OperationTimer:
    #Initial Variables
    def __init__(self, elements, setting):
        self._elements = elements
        #Toggle Data Structure Creation
        #Create a Stack
        if setting == 0:
            self._stack = self._stack_create()
        #Create a LinkedList
        elif setting == 1:
            self._linkedlist = self._linkedlist_create()
        #Create a MaxHeap
        elif setting == 2:
            self._maxheap = self._maxheap_create()
        #Create a Binary Search Tree
        elif setting == 3:
            self._binarytree = self._binarytree_create()
        #No Data Structure Creation
        else:
            pass

    #[Stack] Create Operation
    def _stack_create(self):
        #Creating the Stack
        my_stack = Stack()
        #Pushing All Elements
        for num in self._elements:
            my_stack.push(num)
        return my_stack

    #[LinkedList] Create Operation
    def _linkedlist_create(self):
        #Initial Variables
        i = 0

        #Creating the LinkedList
        my_linkedlist = LinkedList()
        #Inserting All Elements
        for num in self._elements:
            my_linkedlist.insert(i, num)
            i += 1
        return my_linkedlist
    
    #[MaxHeap] Create Operation
    def _maxheap_create(self):
        #Creating the MaxHeap
        my_maxheap = MaxHeap()
        #Add All Elements
        for num in self._elements:
            my_maxheap.add(num)
        return my_maxheap

    #[BinaryTree] Create Operation
    def _binarytree_create(self):
        #Creating the BinaryTree
        my_binarytree = BinaryTree()
        #Add All Elements
        for num in self._elements:
            my_binarytree.add(num)
        return my_binarytree

    #[General] Value Create Operation
    def _generate_value(self):
        value = random.randint(0, 999999)
        return value

    #[Stack] Single Pop Operation
    def single_stack(self):
        self._stack.pop()
        return True

    #[Stack] All Pop Operation
    def all_stack(self):
        while not self._stack.is_empty():
            self._stack.pop()
        return True
    
    #[LinkedQueue] Enqueue All Operation
    def queue_enqueue(self):
        my_queue = LinkedQueue()
        for num in self._elements:
            my_queue.enqueue(num)
        return True
    
    #[LinkedList] Last Entry Operation
    def linkedlist_last_entry(self):
        last_entry = self._linkedlist.length()
        self._linkedlist.get_entry(last_entry)
        return True

    #[LinkedList] All Entry Operation
    def linkedlist_all_entry(self):
        #Initial Variables
        print_list = []
        #Operation Start
        last_index = self._linkedlist.length()
        for index in range(0, last_index):
            entry_data = self._linkedlist.get_entry(index)
            print_list.append(str(entry_data))
        #Print All Elements
        print(' '.join(print_list))
        return True

    #[MaxHeap] Add Value Operation
    def maxheap_add(self):
        add_value = self._generate_value()
        self._maxheap.add(add_value)
        return True
    
    #[BinaryTree] Search Operation
    def binarytree_search(self):
        search_value = self._generate_value()
        self._binarytree.search(search_value)
        return True


