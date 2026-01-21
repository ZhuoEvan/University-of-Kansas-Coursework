#linkedqueue.py

from node import Node

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry):
        pass

    def dequeue(self):
        pass

    def peek_front(self):
        if self._is_empty():
            raise RuntimeError
        else:
            return self._front

    def is_empty(self):
        return self._front is None
