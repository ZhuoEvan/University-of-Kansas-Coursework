'''
Author: Evan Zhuo
KUID: 3109819
Date: 04/09/2024
Lab: lab09
Last modified: 04/14/2024
Purpose: Defining Circle Type and Creating a Driver
'''
#Short Note on Lab Documentation
'''
Evan Zhuo's goofy small brain never realized that documentation
meant explaining how the code functions.
Now for the pentultimate and final lab, goofy Evan Zhuo
will remember to document the code. :)
'''
#Global Import of the Circle Class 
from circle import Circle

#Global Variables
bar = '===================='

#Functions
def create_user_circle():
    circle = Circle()
    print(f'{bar}\nEnter information for Circle:')
    circle.radius = float(input('Radius: '))
    circle.x_pos = float(input('X Position: '))
    circle.y_pos = float(input('Y Position: '))
    print(f'{bar}\n')
    return circle
    
def print_circle_info(circ, name='Circle'):
    #Printing Circle Member Methods
    print(f'{bar}\nInformation for {name}:')
    print(f'location: ({circ.x_pos}, {circ.y_pos})')
    print(f'diameter: {circ.diameter()}')
    print(f'area: {circ.area()}')
    print(f'circumference: {circ.circumference()}')
    print(f'distance from the origin: {circ.dist_to_origin()}')
    print(f'{bar}\n')
    
def main():
    #Declaring an Instance of Circle Class
    circle_a = Circle()
    circle_b = Circle()

    #Creating Circles
    circle_a = create_user_circle()
    
    #User Decision on Naming the Circles
    name_check = input('Would you like to name this circle? (y/n): ')
    if name_check.lower() == 'y':
        circle_a_name = input('Enter a name for this Circle: ')
        if len(circle_a_name) == 0:
            circle_a_name = 'Circle A'
    else:
        #Circle name will be Circle X if user does not want to name
        circle_a_name = 'Circle A'
    print('\n')
    circle_b = create_user_circle()
    name_check = input('Would you like to name this circle? (y/n): ')
    if name_check.lower() == 'y':
        circle_b_name = input('Enter a name for this Circle: ')
        if len(circle_b_name) == 0:
            circle_b_name = 'Circle B'
    else:
        circle_b_name = 'Circle B'
    print('\n')
    
    #Printing Both Circles' Information
    print_circle_info(circle_a, circle_a_name)
    print_circle_info(circle_b, circle_b_name)

    #Is_Inside and Is_Overlap Checks
    print(f'{bar}\nInformation Regarding Both Circles:')
    if circle_a.is_inside(circle_b) is True:
        print(f'\tInside [TRUE]')
    else:
        print(f'\tInside [FALSE]')
    if circle_a.is_overlap(circle_b) is True:
        print(f'\tOverlap [TRUE]')
    else:
        print(f'\tOverlap [FALSE]')
    print(f'{bar}\n')
    
    #Prompt to Exit
    input('Press Enter Key to Exit the Program.')
main()
