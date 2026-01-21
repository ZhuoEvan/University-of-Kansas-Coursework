'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/05/2024
Lab: lab07
Last modified: 11/13/2024
Purpose: Binary Search Tree Interactive Class
'''
#controlcenter.py

from binarytree import BinaryTree
from pokemon import Pokemon

class ControlCenter:
    #Initial Variables
    def __init__(self, dex):
        self._dex = dex
        self.my_tree = BinaryTree()
        self._copy_exist = 0
        self.my_tree_copy = BinaryTree()
    
    #Program Main Menu
    def _menu(self):
        menu = '===== Menu =====\n1) Add\n2) Search\n3) Print\n'
        menu += '4) Remove\n5) Copy\n6) Quit\n================\n'
        return menu

    #Program Copy Menu
    def _copy_menu(self):
        menu = '=== Pick Tree ===\n1) Original\n2) Copy\n'
        menu += '=================\n'
        return menu

    #Add Function
    def _add(self):
        #Initial Variables
        progress_gate = 0
        copy_mode = 0

        #Switch to Copy Tree if Copy BST exists
        if self._copy_exist == 1:
            print(self._copy_menu())
            toggle_copy = input('Select an Option: ')
            if toggle_copy.lower() == 'original' or toggle_copy == '1':
                copy_mode = 0
            elif toggle_copy.lower() == 'copy' or toggle_copy == '2':
                copy_mode = 1
            else:
                print('Invalid Input\nAutomatically using Original Tree')

        #Creating A New Entry to Add to BST
        print('[Create a New Entry]')
        while progress_gate != 3:
            try:
                if progress_gate == 0:
                    user_en_name = input('Enter the English Name for New Entry: ')
                    progress_gate = 1
                #Valid Integer Input Gate
                if progress_gate == 1:
                    user_poke_id = int(input('Enter the Pokedex Number for New Entry: '))
                    user_jp_name = input('Enter the Japanese Name for New Entry: ')
                    progress_gate = 2
                #Confirmation Gate
                if progress_gate == 2:
                    print(f'================\n[New Entry Data: {user_en_name} | {user_poke_id} | {user_jp_name}]')
                    print('*Inputting "N" will reset the New Entry\n================')
                    confirm = input('Confirm Addition? (Y/N): ')
                    if confirm.lower() == 'y':
                        progress_gate = 3
                    #Reset Entry
                    else:
                        progress_gate = 0
            except:
                print('Invalid Input')
        try:
            #Putting Inputs into Pokemon Class and Adding the Class to the Binary Search Tree
            add_pokemon = Pokemon(user_en_name, user_poke_id, user_jp_name)
            #Determine which Binary Search Tree the New Entry is Added To
            if copy_mode == 1:
                self.my_tree_copy.add(add_pokemon)
            else:
                self.my_tree.add(add_pokemon)
        except:
            print('Unable to Add: Duplicate Values')

    #Search Function
    def _search(self):
        #Initial Variables
        search_gate = 0
        copy_mode = 0

        #Switch to Copy Tree if Copy BST exists
        if self._copy_exist == 1:
            print(self._copy_menu())
            toggle_copy = input('Select an Option: ')
            if toggle_copy.lower() == 'original' or toggle_copy == '1':
                copy_mode = 0
            elif toggle_copy.lower() == 'copy' or toggle_copy == '2':
                copy_mode = 1
            else:
                print('Invalid Input\nAutomatically using Original Tree')
            
        while search_gate == 0:
            try:
                #Ask User for Search Pokemon Number
                print('[Search for a Pokemon using Pokedex Number]')
                search_id = int(input('Pokedex Number: '))
                #Determine which Binary Search Tree to Search in
                if copy_mode == 1:
                    search_value = self.my_tree_copy.search(search_id)
                else:
                    search_value = self.my_tree.search(search_id)
                search_gate = 1
            #Error Check: Invalid Input
            except ValueError:
                print('Invalid Input: Not a Pokedex Number')
        #Print the Output of the Search Function
        if search_value is False:
            print('This Pokemon is not in the Binary Search Tree')
        else:
            print(f'Pokedex Number {search_id} Pokemon:\n{search_value}')

    #Print Function
    def _print(self):
        #Initial Variables
        print_gate = 0
        copy_mode = 0

        #Switch to Copy Tree if Copy BST exists
        if self._copy_exist == 1:
            print(self._copy_menu())
            toggle_copy = input('Select an Option: ')
            if toggle_copy.lower() == 'original' or toggle_copy == '1':
                copy_mode = 0
            elif toggle_copy.lower() == 'copy' or toggle_copy == '2':
                copy_mode = 1
            else:
                print('Invalid Input\nAutomatically using Original Tree')
            
        while print_gate == 0:
                try:
                    print('=== Print Menu ===\n1) Pre Order\n2) In Order\n3) Post Order\n==================')
                    user_select = input('Enter an option: ')
                    if user_select == '1' or 'pre' in user_select.lower() and len(user_select) < 15:
                        #PreOrder Print with Copy of Binary Search Tree
                        if copy_mode == 1:
                            self.my_tree_copy.print_order(self.my_tree_copy.preorder)
                        #PreOrder Print with Original Binary Search Tree
                        else:
                            self.my_tree.print_order(self.my_tree.preorder)
                        print_gate = 1
                            
                    elif user_select == '2' or 'in' in user_select.lower() and len(user_select) < 15:
                        #InOrder Print with Copy of Binary Search Tree
                        if copy_mode == 1:
                            self.my_tree_copy.print_order(self.my_tree_copy.inorder)
                        #InOrder Print with Original Binary Search Tree
                        else:
                            self.my_tree.print_order(self.my_tree.inorder)
                        print_gate = 1
                            
                    elif user_select == '3' or 'post' in user_select.lower() and len(user_select) < 15:
                        #PostOrder Print with Copy of Binary Search Tree
                        if copy_mode == 1:
                            self.my_tree_copy.print_order(self.my_tree_copy.postorder)
                        #PostOrder Print with Original Binary Search Tree
                        else:
                            self.my_tree.print_order(self.my_tree.postorder)
                        print_gate = 1

                    #Error Check: Invalid Input   
                    else:
                        raise RuntimeError
                except:
                    print('Invalid Input')

    #Remove Function
    def _remove(self):
        #Initial Variables
        remove_gate = 0
        copy_mode = 0

        #Switch to Copy Tree if Copy BST exists
        if self._copy_exist == 1:
            print(self._copy_menu())
            toggle_copy = input('Select an Option: ')
            if toggle_copy.lower() == 'original' or toggle_copy == '1':
                copy_mode = 0
            elif toggle_copy.lower() == 'copy' or toggle_copy == '2':
                copy_mode = 1
            else:
                print('Invalid Input\nAutomatically using Original Tree')

        while remove_gate == 0:
            try:
                #Ask User for Remove Pokemon Number
                print('[Remove a Pokemon using Pokedex Number]')
                remove_id = int(input('Pokedex Number: '))
                #Determine which Binary Search Tree to Search in
                #To Confirm Pokemon Exist in Binary Search Tree
                if copy_mode == 1:
                    remove_value = self.my_tree_copy.search(remove_id)
                else:
                    remove_value = self.my_tree.search(remove_id)
                remove_gate = 1
            #Error Check: Invalid Input
            except ValueError:
                print('Invalid Input: Not a Pokedex Number')

        #Error Check: Not in Binary Search Tree
        if remove_value is False:
            print('This Pokemon is not in the Binary Search Tree')
        else:
            print(f'Pokemon: {remove_value} is being removed...')
            #Determine which Binary Search Tree to Remove in
            if copy_mode == 1:
                self.my_tree_copy.remove(remove_id)
            else:
                self.my_tree.remove(remove_id)
            print(f'Pokedex Number {remove_id} has been removed.')
            
    #Copy Function
    def _copy(self):
        if self.my_tree_copy._root is None:
            print('Copying the Current Binary Search Tree...')
            self.my_tree.preorder(self.my_tree.visit_function)
            #Appending each element into Copy Binary Search Tree
            for element in self.my_tree._traversal:
                self.my_tree_copy.add(element)
            print('A Copy of the Current Binary Search Tree has been Created\n')
            self._copy_exist = 1
        else:
            print('Copy already exist!\nUse other functions')

    #Run the Program
    def run(self):
        #Initial Variables
        gate = 0

        #Automatically Add Items into Original Binary Search Tree
        print('Adding File Content into Binary Search Tree...')
        for pokemon in self._dex:
            self.my_tree.add(pokemon)
        print('File Content has been transfered to Binary Search Tree\n')

        #Choice Selection
        while gate != 1:
            try:
                print(self._menu())
                user_choice = input('Select an Option: ')

                #Add Function
                if user_choice.lower() == 'add' or user_choice == '1':
                    self._add()
                #Search Function
                elif user_choice.lower() == 'search' or user_choice == '2':
                    self._search()
                #Print Function
                elif user_choice.lower() == 'print' or user_choice == '3':
                    self._print()
                #Remove Function
                elif user_choice.lower() == 'remove' or user_choice == '4':
                    self._remove()
                #Copy Function
                elif user_choice.lower() == 'copy' or user_choice == '5':
                    self._copy()
                #Quit the Program
                elif user_choice.lower() == 'quit' or user_choice == '6':
                    gate = 1

                #Error Check: Invalid Input
                else:
                    raise RuntimeError
            except:
                print('Invalid Option')
        #Exit Program Statement
        print('Exiting the Program...')
