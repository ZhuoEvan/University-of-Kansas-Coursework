'''
Author: Evan Zhuo
KUID: 3109819
Date: 04/09/2024
Lab: lab09
Last modified: 04/14/2024
Purpose: Defining Circle Class
'''
#Importing pi to use for the functions
from math import pi

#Defining the Circle Class
class Circle:
    #
    def __init__(self):
        self._radius = 0
        self._x_pos = 0
        self._y_pos = 0
        
    #Circle Diameter Equation
    def diameter(self):
        return 2*self.radius

    #Circle Area Equation
    def area(self):
        return (pi*self.radius**2)

    #Circle Circumference Equation
    def circumference(self):
        return (2*pi*self.radius)

    #Distance Equation
    def dist_to_origin(self):
        return ((self.x_pos**2 + self.y_pos**2)**0.5)

    #Distance Equation but between Two Circles
    def dist_to_center(self, other):
        return (((other.x_pos - self.x_pos)**2 + (other.y_pos - self.y_pos)**2)**0.5)

    #Compares Distance and the Difference of the Two Circles' Radius to find Is_Inside
    def is_inside(self, other_circle):
        if self.dist_to_center(other_circle) <= self.radius - other_circle.radius:
            return True
        elif self.dist_to_center(other_circle) <= other_circle.radius - self.radius:
            return True
        else:
            return False

    #Compares Distance and the Sum of the Two Circles' Radius to find Overlap
    def is_overlap(self, other_circle):
        if self.dist_to_center(other_circle) <= self.radius + other_circle.radius:
            return True
        else:
            return False
    
