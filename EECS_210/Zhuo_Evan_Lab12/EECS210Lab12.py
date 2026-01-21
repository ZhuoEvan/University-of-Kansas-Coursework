'''
Name: Evan Zhuo
KUID: 3109819
LAB Session: Friday 11 a.m.
LAB Assignment: 12
Description: Prefix Form to Postfix Form
Collaborators: None
'''
#EECS210Lab12.py

#Instruction Function
def instruction():
    inst = '====================\n'
    inst += 'Enter a SPACE-SEPERATED Prefix-Form Input.\n'
    inst += '===================='
    return inst

#Space Split Function
def space_split(unsplit_string):
    split_list = unsplit_string.strip().split(' ')
    return split_list

#Check Next Function
def valid_next(full_list, next_int):
    #Check Next Index is In Bounds
    if next_int >= len(full_list):
        return False
    else:
        #Check Next Element is Variable
        if _is_variable(full_list, next_int) is True:
            return True
        else:
            return False

#Check Variable Function
def _is_variable(full_list, index):
    #Initial Variables
    operations = ['+', '-', '*', '/', '^']

    #Check if next element is a variable
    if full_list[index] in operations:
        return False
    else:
        return True

#Postfix Function
def postfix_create(full_list):
    #Initial Variables
    operation_stack = []
    output_list = []
    operations = ['+', '-', '*', '/', '^']
    next_toggle = 0

    #Pass through all elements inside the full list
    for index in range(0, len(full_list)):
        #Append Operation into Operation Stack
        if full_list[index] in operations:
            operation_stack.append(full_list[index])

        #Variables Cases
        else:
            #Append Second Child and Parent Node
            if next_toggle == 1:
                output_list.append(full_list[index])
                output_list.append(operation_stack.pop())
                #Reset Next Toggle
                next_toggle = 0
            #Append First Child Node Cases
            else:
                output_list.append(full_list[index])
                #Check for Second Child Node
                if valid_next(full_list, index + 1) is True:
                    next_toggle = 1
                #Append Parent Node to Only Child Node
                else:
                    output_list.append(operation_stack.pop())

    #Append Remaining Operations
    if operation_stack != 0:
        for oper in operation_stack:
            output_list.append(oper)

    #Return Output to Main
    return output_list

#Main Function
def main():
    #Receive User Input
    print(instruction())
    user_input = input('Input: ')

    #Send User Input into Split Function
    full_list = space_split(user_input)

    #Send Full List into Postfix Create Function
    output = postfix_create(full_list)

    #Print the Postfix Output
    connected_output = ' '.join(output)
    print(f'Output: {connected_output}')

main()