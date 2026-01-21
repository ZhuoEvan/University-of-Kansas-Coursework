'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/30/2024
Lab: lab04
Last modified: 10/4/2024
Purpose: Fibonacci Recursion Exercise
'''
#exercise3.py

def main():
    #Error Check: Valid Inputs
    error_check_gate = False
    while error_check_gate == False:
        #try-except block will repeat until given valid inputs
        try:
            initial_value = input('Enter mode and value: -')
            separated_value = initial_value.split(' ')
            mode = separated_value[0]  
            #Error Check: Valid Modes
            if mode.lower() != 'i' and mode.lower() != 'v':
                raise RuntimeError
            #Error Check: Valid Integer
            value = int(separated_value[1])
            if value < 0:
                raise ZeroDivisionError
            
            #Proceed with the Code
            error_check_gate = True
            
        #Except block provides reason for Invalid Input
        except RuntimeError:
            print(f'The mode input {mode} is not "i" or "v"')
        except ValueError:
            print('The value input is not an integer')
        except ZeroDivisionError:
            print(f'The value input {value} is not a positive number')
            
    #Send the inputs into mode_selection function
    mode_selection(mode, value)
    input('\nPress the Enter Key to Exit the Program\n')

#Mode Selection Function   
def mode_selection(mode, value):
    #ith mode
    if mode.lower() == 'i':
        ith = fibonacci(value)
        print(ith)
        return
    
    #verify mode
    else:
        verify_mode_value = 0
        verify = verify_mode(verify_mode_value, value)
        #Verify value is in the fibonacci sequence
        if verify == True:
            print(f'{value} is in the sequence')
            return
        #Verify value is not in the fibonacci sequence
        else:
            print(f'{value} is not in the sequence')
            return

#Fibonacci Function
def fibonacci(value):
    #Return 0 or 1
    if value <= 1:
        return value
    else:
        #Adding the previous value and the previous-previous value
        #0 and 1 will be added first
        result = fibonacci(value - 1) + fibonacci(value - 2)
        return result

#Verify Mode Function
def verify_mode(value, verify_value):
    #Receiving the fibonacci value from fibonacci function
    fibonacci_number = fibonacci(value)
    
    #Keep Checking the fibonnaci sequence until fibonacci number
    #is less than or equal to the verify value
    if verify_value > fibonacci_number:
        #Increase the value to get the next number in the fibonacci sequence
        value += 1
        return verify_mode(value, verify_value)
    #Verify value is in the sequence scenario
    elif verify_value == fibonacci_number:
        return True
    #Verify value is not in the sequence scenario
    else:
        return False
        
main()
