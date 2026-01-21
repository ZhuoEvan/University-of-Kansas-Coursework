'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/28/2024
Lab: lab06
Last modified: 11/04/2024
Purpose: Binary Tree Class
'''
#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    #Initial Variables
    def __init__(self):
        self._root = None
        self._visited_nodes = []

    #Binary Tree Add Function
    def add(self, entree):
        if self._root is None:
            self._root = BinaryNode(entree)
        else:
            self._rec_add(entree, self._root)

    #Hidden Binary Tree Recursive Add Function
    def _rec_add(self, entree, current_node):
        if entree == current_node.entree:
            raise ValueError('Duplicate Values')
        elif entree < current_node.entree:
            if current_node.left is None:
                current_node.left = BinaryNode(entree)
            else:
                self._rec_add(entree, current_node.left)
        elif entree > current_node.entree:
            if current_node.right is None:
                current_node.right = BinaryNode(entree)
            else:
                self._rec_add(entree, current_node.right)

    #Binary Tree Search Function (Unused)
    def search(self, target):
        return self._rec_search(target, self._root)

    #Hidden Binary Tree Recursive Search Function (Unused)
    def _rec_search(self, target, current_node):
        if current_node is None:
            return False
        elif current_node.entree == target:
            return current_node
        elif target < current_node.entree:
            return self._rec_search(target, current_node.left) 
        else:
            return self._rec_search(target, current_node.right)
    
    #Visit Function
    def visit_function(self, current_node):
        self._visited_nodes.append(current_node.entree)

    #PreOrder Traversal Order
    def preorder(self, visit_function):
        self._rec_preorder(visit_function, self._root)

    def _rec_preorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            visit_function(current_node)
            self._rec_preorder(visit_function, current_node.left)
            self._rec_preorder(visit_function, current_node.right)
    
    #InOrder Traversal Order
    def inorder(self, visit_function):
        self._rec_inorder(visit_function, self._root)

    def _rec_inorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            self._rec_inorder(visit_function, current_node.left)
            visit_function(current_node)
            self._rec_inorder(visit_function, current_node.right)

    #PostOrder Traversal Order
    def postorder(self, visit_function):
        self._rec_postorder(visit_function, self._root)

    def _rec_postorder(self, visit_function, current_node):
        if current_node == None:
            return
        else:
            self._rec_postorder(visit_function, current_node.left)
            self._rec_postorder(visit_function, current_node.right)
            visit_function(current_node)

    def run(self, function):
        #Add List Function
        if function == 'add':
            user_list = input('Enter a comma-separated list of numbers: ')
            print('Adding the number(s) into the Binary Search Tree...')
            element_list = []

            #Cleaning the elements that will go into the Binary Search Tree
            draft_element_list = user_list.split(',')
            for draft_element in draft_element_list:
                element = draft_element.strip()
                element_list.append(int(element))
            
            #Adding to the Binary Search Tree using add function
            for element in element_list:
                self.add(element)
            print('Number(s) have been added to the Binary Search Tree')

        #Print Order Function  
        elif function == 'print':
            print_gate = 0
            quit_gate = 0
            self._visited_nodes = []

            #User Selects the order of printing
            while print_gate == 0:
                try:
                    print(self.print_menu())
                    user_select = input('Enter an option: ')
                    #User entered 1 or preorder
                    if user_select == '1' or 'pre' in user_select.lower() and len(user_select) < 15:
                        self.preorder(self.visit_function)
                        print_gate = 1
                    
                    #User entered 2 or inorder
                    elif user_select == '2' or 'in' in user_select.lower() and len(user_select) < 15:
                        self.inorder(self.visit_function)
                        print_gate = 1
                    
                    #User entered 3 or postorder
                    elif user_select == '3' or 'post' in user_select.lower() and len(user_select) < 15:
                        self.postorder(self.visit_function)
                        print_gate = 1

                    #User entered 4 or quit to return back to main menu
                    elif user_select == '4' or user_select.lower() == 'quit':
                        quit_gate = 1
                        print_gate = 1 

                    #User inputs an unregistered value
                    else:
                        raise ValueError
                except:
                    print('Enter a Valid Input')

            #Printing the visited node order
            if quit_gate == 0:
                if len(self._visited_nodes) == 0:
                    print('Visit Order:\nEmpty Tree')
                else:
                    print(f'Visit Order:\n{self._visited_nodes}')
            else:
                print('Exiting Print Order Function...')

        #Reset Function
        elif function == 'reset':
            self._root = None
            self._visited_nodes = []
            print('Binary Search Tree has been resetted.\n')
            
        else:
            raise RuntimeError('Program has encountered an unexpected error')
    
    #Order Select Menu
    def print_menu(self):
        output = '=== Print Menu ===\n'
        output += '1) Pre Order\n'
        output += '2) In Order\n'
        output += '3) Post Order\n'
        output += '4) Quit\n'
        output += '=================='
        return output
        
