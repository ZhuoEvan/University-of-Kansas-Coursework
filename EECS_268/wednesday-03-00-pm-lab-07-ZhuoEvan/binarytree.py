'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/05/2024
Lab: lab07
Last modified: 11/13/2024
Purpose: Binary Search Tree Class
'''
#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None
        self._traversal = []
    
    #Binary Tree Add Function
    def add(self, entry):
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    #Hidden Binary Tree Recursive Add Function
    def _rec_add(self, entry, cur_node):
        if entry == cur_node.entry:
            raise RuntimeError('Duplicate Values')
        elif entry < cur_node.entry:
            if cur_node.left is None:
                cur_node.left = BinaryNode(entry)
            else:
                self._rec_add(entry, cur_node.left)
        elif entry > cur_node.entry:
            if cur_node.right is None:
                cur_node.right = BinaryNode(entry)
            else:
                self._rec_add(entry, cur_node.right)

    #Binary Tree Search Function
    def search(self, target):
        return self._rec_search(target, self._root)

    #Hidden Binary Tree Recursive Search Function
    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry.poke_id == target:
            return cur_node
        elif target < cur_node.entry.poke_id:
            return self._rec_search(target, cur_node.left) 
        else:
            return self._rec_search(target, cur_node.right)
    
    #Remove Function
    def remove(self, target):
        #Create a list of numbers to keep in BST
        unremove_list = []
        remove_node = self.search(target)
        self.preorder(self.visit_function)
        #Append all elements except the removed element
        for element in self._traversal:
            if remove_node.entry.poke_id != element.poke_id:
                unremove_list.append(element)
        #Reset the Binary Search Tree
        self._root = None
        #Re-Add all unremoved elements into the Binary Search Tree
        for unremove in unremove_list:
            self.add(unremove)
            
    #Visit Function
    def visit_function(self, cur_node):
        self._traversal.append(cur_node.entry)

    #PreOrder Print Function
    def preorder(self, visit_function):
        #Reset the traversal order list
        self._traversal = []
        self._rec_preorder(visit_function, self._root)
    
    #Hidden PreOrder Print Function
    def _rec_preorder(self, visit_function, cur_node):
        if cur_node is None:
            return
        else:
            visit_function(cur_node)
            self._rec_preorder(visit_function, cur_node.left)
            self._rec_preorder(visit_function, cur_node.right)
    
    #InOrder Print Function
    def inorder(self, visit_function):
        #Reset the traversal order list
        self._traversal = []
        self._rec_inorder(visit_function, self._root)

    #Hidden InOrder Print Function
    def _rec_inorder(self, visit_function, cur_node):
        if cur_node is None:
            return
        else:
            self._rec_inorder(visit_function, cur_node.left)
            visit_function(cur_node)
            self._rec_inorder(visit_function, cur_node.right)
    
    #PostOrder Print Function
    def postorder(self, visit_function):
        #Reset the traversal order list
        self._traversal = []
        self._rec_postorder(visit_function, self._root)

    #Hidden PostOrder Print Function
    def _rec_postorder(self, visit_function, cur_node):
        if cur_node is None:
            return
        else:
            self._rec_postorder(visit_function, cur_node.left)
            self._rec_postorder(visit_function, cur_node.right)
            visit_function(cur_node)
    
    #Print Order Selection Function
    def print_order(self, order):
        order(self.visit_function)

        #Printing the traversal order
        for element in self._traversal:
            print(element)