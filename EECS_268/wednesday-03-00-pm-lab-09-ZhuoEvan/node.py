'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Node Class
'''
#node.py

class Node:
    #Initializing Node Class
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    #String of a Node
    def __str__(self):
        output = f'{self.entry}'
        return output

    #Representation of a Node
    def __repr__(self):
        output = f'{self.entry}'
        return output