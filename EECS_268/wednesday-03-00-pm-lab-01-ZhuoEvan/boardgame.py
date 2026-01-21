'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/11/2024
Lab: lab01
Last modified: 9/15/2024
Purpose: Setting Infomation to Board Games
'''
#boardgame.py

class BoardGame:
    #Initial Values
    def __init__(self, name, rating, baverage, avgweight, year, bbgbestplayers):
        self._name = name
        self._rating = rating
        self._baverage = baverage
        self._avgweight = avgweight
        self._year = year
        self._bbgbestplayers = bbgbestplayers

    #Less Than Operator
    def __lt__(self, other):
        if self._rating < other._rating:
            return True
        else:
            return False

    #Greater Than Operator        
    def __gt__(self, other):
        if self._rating > other._rating:
            return True
        else:
            return False

    #Less Than or Equal to Operator
    def __le__(self, other):
        if self._rating <= other._rating:
            return True
        else:
            return False

    #Greater Than or Equal to Operator
    def __ge__(self, other):
        if self._rating >= other._rating:
            return True
        else:
            return False

    #Equal to Operator        
    def __eq__(self, other):
        if self._rating == other._rating:
            return True
        else:
            return False

    #Not Equal to Operator
    def __ne__(self, other):
        if self._rating != other._rating:
            return True
        else:
            return False

    #String Operator       
    def __str__(self):
        output = f'============\n{self._name}\n{self._rating}\n'
        output += f'{self._baverage}\n{self._avgweight}\n{self._year}\n'
        output += f'{self._bbgbestplayers}\n============'
        return output

    #Representation Operator
    def __repr__(self):
        output = f'============\n{self._name}\n{self._rating}\n'
        output += f'{self._baverage}\n{self._avgweight}\n{self._year}\n'
        output += f'{self._bbgbestplayers}\n============'
        return output
