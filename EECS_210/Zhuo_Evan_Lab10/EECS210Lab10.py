'''
Name: Evan Zhuo
KUID: 3109819
LAB Session: Friday 11 a.m.
LAB Assignment: 10
Description: Euler Circuit
Collaborators: None
'''

#EECS210Lab10.py

#Output Function
def output(cur_output, cur_col):
    #Alphabet Assignment
    if cur_col == 0:
        cur_output.append('a')
    elif cur_col == 1:
        cur_output.append('b')
    elif cur_col == 2:
        cur_output.append('c')
    elif cur_col == 3:
        cur_output.append('d')
    elif cur_col == 4:
        cur_output.append('e')
    elif cur_col == 5:
        cur_output.append('f')
    elif cur_col == 6:
        cur_output.append('g')
    elif cur_col == 7:
        cur_output.append('h')
    elif cur_col == 8:
        cur_output.append('i')
    elif cur_col == 9:
        cur_output.append('j')
    elif cur_col == 10:
        cur_output.append('k')
    elif cur_col == 11:
        cur_output.append('l')
    elif cur_col == 12:
        cur_output.append('m')
    elif cur_col == 13:
        cur_output.append('n')
    elif cur_col == 14:
        cur_output.append('o')
    elif cur_col == 15:
        cur_output.append('p')
    elif cur_col == 16:
        cur_output.append('q')
    elif cur_col == 17:
        cur_output.append('r')
    elif cur_col == 18:
        cur_output.append('s')
    elif cur_col == 19:
        cur_output.append('t')
    elif cur_col == 20:
        cur_output.append('u')
    elif cur_col == 21:
        cur_output.append('v')
    elif cur_col == 22:
        cur_output.append('w')
    elif cur_col == 23:
        cur_output.append('x')
    elif cur_col == 24:
        cur_output.append('y')
    else:
        cur_output.append('z')
    #Return Output List with added element
    return cur_output

#Remove Function
def remove(matrix, cur_row, cur_col):
    matrix[cur_row][cur_col] = 0
    matrix[cur_col][cur_row] = 0
    return matrix

#Circuit Function
def circuit(matrix, cur_row, my_output):
    if len(my_output) != 1:
        if my_output[0] == my_output[-1]:
            return my_output
    #Base Case
    for i in range(0, len(matrix)):
        if int(matrix[cur_row][i]) == 1:
            my_output = output(my_output, i)
            matrix = remove(matrix, cur_row, i)
            circuit(matrix, i, my_output)
    return my_output
    
#Build Function
def build(n):
    #Initial Variables
    matrix_gate = 0

    #While Loop to build proper matrix
    while matrix_gate != n:
        try:
            #Main Variables
            matrix = []
            matrix_gate = 0
            #Getting Matrix Row from User
            for i in range(0, n):
                print(f'Enter a space-separated row ({i+1}/{n})')
                #Splitting into individual elements
                draft_row = input('Row: ')
                row = draft_row.split(' ')
                #Error Check: Valid Row Size
                if len(row) == n:
                    matrix.append(row)
                    matrix_gate += 1
                else:
                    raise RuntimeError
        except:
            print('Row Size does not match n value')
            print('Resetting Matrix...')
    
    #Return completed matrix to main
    return matrix

#Main Function
def main():
    #Receive User n Value
    n = int(input('Enter n value: '))
    #Build n x n Matrix
    my_matrix = build(n)
    my_output = []
    my_output = output(my_output, 0)
    my_circuit = circuit(my_matrix, 0, my_output)
    print(f'Output: {my_circuit}')

main()