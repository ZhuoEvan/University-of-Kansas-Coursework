'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/30/2024
Lab: lab04
Last modified: 10/4/2024
Purpose: Power Function Recursion Exercise
'''
#exercise1.py

def main():
    #Error Check: Valid Inputs
    error_check_gate = False
    #base_gate and power_gate prevents asking the user
    #for another input if given a valid input
    base_gate = False 
    power_gate = False
    #funny flame countdown that contributes nothing to this lab
    flame_countdown = 0
    while error_check_gate == False:
        #try-except block will repeat until given valid inputs
        try:
            #base input
            while base_gate == False:
                base = int(input('Enter a base: '))
                base_gate = True
            #power input
            while power_gate == False:
                power = int(input('Enter a power: '))
                #Error Check: Positive or Zero Integer
                if power < 0:
                    raise RuntimeError
                else:
                    power_gate = True
            error_check_gate = True

        #except-block for Errors
        #Base or Power is not an Integer
        except ValueError:
            print('Enter a valid integer\n')
            flame_countdown += 1
            if flame_countdown == 5:
                print(error_flame())
                flame_countdown = 0
        #Exponent is a Negative Error
        except RuntimeError:
            print('Sorry, your exponent must be zero or larger\n')
            flame_countdown += 1
            if flame_countdown == 5:
                print(error_flame())
                flame_countdown = 0

    #Send the base and power into the power_function
    power_product = power_function(base, power)
    print(power_product)

#An Optional Function
def error_flame():
    flame = '====================\n'
    flame += 'You have been given multiple errors\n'
    flame += 'and yet you managed to type an '
    flame += 'another invalid input.\n'
    flame += 'Just How?!?\n'
    flame += '====================\n'
    return flame

#Power Function
def power_function(base, power):
    #initial answer is 1
    answer = 1
    #Recursion until power is 0
    if power != 0:
        answer = base*power_function(base, power - 1)
    return answer
    
main()
