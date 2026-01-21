'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/05/2024
Lab: lab07
Last modified: 11/13/2024
Purpose: Binary Node Class
'''
#binarynode.py

class BinaryNode:
    #Initial Variables
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
    
    #String Operator
    def __str__(self):
        output = f'{self.entry}'
        return output
    
    #Representation Operator
    def __repr__(self):
        output = f'{self.entry}'
        return output