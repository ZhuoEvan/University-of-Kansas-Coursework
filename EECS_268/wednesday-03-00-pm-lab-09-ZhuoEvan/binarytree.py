'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Binary Tree Class
'''
#binarytree.py

from binarynode import BinaryNode
import sys

#Increase Recursion Limit
sys.setrecursionlimit(100000)

class BinaryTree:
    #Initial Variables
    def __init__(self):
        self._root = None
        self._visited_nodes = [] #Unused

    #Binary Tree Add Function
    def add(self, entry):
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    #Hidden Binary Tree Recursive Add Function
    def _rec_add(self, entry, current_node):
        if entry == current_node.entry:
            raise ValueError('Duplicate Values')
        elif entry < current_node.entry:
            if current_node.left is None:
                current_node.left = BinaryNode(entry)
            else:
                self._rec_add(entry, current_node.left)
        elif entry > current_node.entry:
            if current_node.right is None:
                current_node.right = BinaryNode(entry)
            else:
                self._rec_add(entry, current_node.right)

    #Binary Tree Search Function
    def search(self, target):
        return self._rec_search(target, self._root)

    #Hidden Binary Tree Recursive Search Function
    def _rec_search(self, target, current_node):
        if current_node is None:
            return False
        elif current_node.entry == target:
            return current_node
        elif target < current_node.entry:
            return self._rec_search(target, current_node.left) 
        else:
            return self._rec_search(target, current_node.right)
    
    #Visit Function (Unused)
    def visit_function(self, current_node):
        self._visited_nodes.append(current_node.entry)

    #PreOrder Traversal Order (Unused)
    def preorder(self, visit_function):
        self._rec_preorder(visit_function, self._root)

    def _rec_preorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            visit_function(current_node)
            self._rec_preorder(visit_function, current_node.left)
            self._rec_preorder(visit_function, current_node.right)
    
    #InOrder Traversal Order (Unused)
    def inorder(self, visit_function):
        self._rec_inorder(visit_function, self._root)

    def _rec_inorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            self._rec_inorder(visit_function, current_node.left)
            visit_function(current_node)
            self._rec_inorder(visit_function, current_node.right)

    #PostOrder Traversal Order (Unused)
    def postorder(self, visit_function):
        self._rec_postorder(visit_function, self._root)

    def _rec_postorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            self._rec_postorder(visit_function, current_node.left)
            self._rec_postorder(visit_function, current_node.right)
            visit_function(current_node)