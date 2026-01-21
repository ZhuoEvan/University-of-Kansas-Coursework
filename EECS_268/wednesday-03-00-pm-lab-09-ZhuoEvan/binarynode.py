'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Binary Node Class
'''
#binarynode.py

class BinaryNode:
    #Initial Variables
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None

    #String of a Binary Node
    def __str__(self):
        output = f'{self.entry}'
        return output

    #Representation of a Binary Node
    def __repr__(self):
        output = f'{self.entry}'
        return output