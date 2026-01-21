'''
Name: Evan Zhuo
KUID: 3109819
LAB Session: Friday 11 a.m.
LAB Assignment: 06
Description: Next Permutation in Lexicographic Order
Collaborators: None
'''

#EECS210Lab06.py

def main():
    user_input = input('Input: ')
    my_num_list = []
    for num in user_input:
        my_num_list.append(int(num))
    x = next_permutation(my_num_list)

def next_permutation(number):
    j = len(number) - 2
    k = len(number) - 1
    if number[j] > number[k]:
        number.append(number.pop(j))
        print(number)
    else:
        print(number[j])
        print(number[k])
        
        
    
main()
