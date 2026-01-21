#stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        self._top.next = self._top
        self._top = entry

    def pop(self):
        self._top = self._top.next

    def peek(self):
        return self._top

    def is_empty(self):
        return self._top is None
        
