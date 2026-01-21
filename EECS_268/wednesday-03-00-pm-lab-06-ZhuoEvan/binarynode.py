'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/28/2024
Lab: lab06
Last modified: 11/04/2024
Purpose: Binary Node Class
'''
#binarynode.py

class BinaryNode:
    #Initial Variables
    #Feel free to subtract some points for the terrible en"tree" pun
    def __init__(self, entree):
        self.entree = entree
        self.left = None
        self.right = None

    #String of a Binary Node
    def __str__(self):
        output = f'{self.entree}'
        return output

    #Representation of a Binary Node
    def __repr__(self):
        output = f'{self.entree}'
        return output
