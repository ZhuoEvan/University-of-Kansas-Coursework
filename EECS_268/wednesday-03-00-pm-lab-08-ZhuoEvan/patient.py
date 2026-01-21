'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/13/2024
Lab: lab08
Last modified: 11/18/2024
Purpose: Patient Class
'''
#patient.py

class Patient:
    #Initial Variables
    def __init__(self, first_name, last_name, age, illness, severity, arrival_order):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
        self._illness = illness
        self._severity = severity
        self._arrival_order = arrival_order
    
    #Less Than Operator
    def __lt__(self, other):
        return self._severity < other._severity
    
    #Greater Than Operator
    def __gt__(self, other):
        return self._severity > other._severity
    
    #Greater Than or Equal to Operator
    def __ge__(self, other):
        return self._severity >= other._severity
    
    #Equal to Operator
    def __eq__(self, other):
        return self._severity == other._severity
    
    #String Operator
    def __str__(self):
        output = f'\tName: {self.last_name}, {self.first_name}\n'
        output += f'\tAge: {self._age}\n\tSuffers from: {self._illness}\n'
        output += f'\tIllness severity: {self._severity}\n'
        output += f'\tArrival order: {self._arrival_order}'
        return output

    #Representation Operator
    def __repr__(self):
        output = f'\tName: {self.last_name}, {self.first_name}\n'
        output += f'\tAge: {self._age}\n\tSuffers from: {self._illness}\n'
        output += f'\tIllness severity: {self._severity}\n'
        output += f'\tArrival order: {self._arrival_order}'
        return output