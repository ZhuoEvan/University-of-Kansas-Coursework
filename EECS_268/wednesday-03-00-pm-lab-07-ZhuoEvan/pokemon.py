'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/05/2024
Lab: lab07
Last modified: 11/13/2024
Purpose: Pokemon Class
'''
#pokemon.py

class Pokemon:
    #Initial Variables
    def __init__(self, en_name, poke_id, jp_name):
        self.en_name = en_name
        self.poke_id = poke_id
        self.jp_name = jp_name

    #Less Than Operator
    def __lt__(self, other):
        return self.poke_id < other.poke_id
    
    #Greater Than Operator
    def __gt__(self, other):
        return self.poke_id > other.poke_id
    
    #Less Than or Equal To Operator
    def __le__(self, other):
        return self.poke_id <= other.poke_id
    
    #Greater Than or Equal To Operator
    def __ge__(self, other):
        return self.poke_id >= other.poke_id
    
    #Equal To Operator
    def __eq__(self, other):
        return self.poke_id == other.poke_id
    
    #Not Equal To Operator
    def __ne__(self, other):
        return self.poke_id != other.poke_id

    #String Operator
    def __str__(self):
        output = f'{self.en_name} | {self.poke_id} | {self.jp_name}'
        return output
    
    #Representation Operator
    def __repr__(self):
        output = f'{self.en_name} | {self.poke_id} | {self.jp_name}'
        return output