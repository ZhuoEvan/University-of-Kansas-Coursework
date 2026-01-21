'''
Name: Evan Zhuo
KUID: 3109819
LAB Session: Friday 11 a.m.
LAB Assignment: 11
Description: Dijkstra's Algorithm
Collaborators: None
'''
#EECS210Lab11.py

#Output Function
def output(cur_output, index):
    #Initial Variables
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if isinstance(index, int):
        cur_output.append(alphabet_list[index])
        return cur_output
    else:
        for i in range(0, len(alphabet_list)):
            if index.lower() == alphabet_list[i]:
                cur_output.append(alphabet_list[i])
                return cur_output, i

#Remove Function
def remove(matrix, cost, cur_row, cur_col):
    cost = cost + int(matrix[cur_row][cur_col])
    #Symmetric Removal
    matrix[cur_row][cur_col] = 0
    matrix[cur_col][cur_row] = 0
    #Return Matrix with Removal Completed
    return matrix

#Dijkstra Algorithm Function
def dijkstra(matrix, cur_row, my_output, cost, start, end):
    if start in my_output and end in my_output:
        return my_output
    else:
        for i in range(0, len(matrix)):
            if int(matrix[cur_row][i]) > 0:
                my_output = output(my_output, i)
                matrix = remove(matrix, cost, cur_row, i)
                dijkstra(matrix, i, my_output, cost, start, end)

#Circuit Function
def circuit(matrix, cur_row, my_output):
    #Travel the Circuit (B-Z)
    for i in range(1, len(matrix)):
        if int(matrix[cur_row][i]) == 1:
            #Append Destination
            my_output = output(my_output, i)
            #Symmetric Removal
            matrix = remove(matrix, cur_row, i)
            #Recursion at Row i
            circuit(matrix, i, my_output)
    #Travel the Circuit (Exclusive A)
    if int(matrix[cur_row][0]) == 1:
        #Append Destination
        my_output = output(my_output, 0)
        #Symmetric Removal
        matrix = remove(matrix, cur_row, 0)
        #Recursion at Row 0
        circuit(matrix, 0, my_output)
    #Return Output List
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
    #Initial Variables
    my_output = []

    #Receive User n Value
    n = int(input('Enter n value: '))
    #Receive User Desired Path
    start_point = input('Starting Point Input: ')
    end_point = input('Ending Point Input: ')

    #Build n x n Matrix
    my_matrix = build(n)
    #-1 is infinity and 0 will be path traveled
    #similar to eecs 268 lab 5
    #Add the Start Point and Get the Start Index from Output Function
    my_output, start_index = output(my_output, start_point)
    my_dijkstra = dijkstra(my_matrix, start_index, my_output, 0, start_point, end_point)
    #Print Output
    print(f'Output: {my_dijkstra}')

main()