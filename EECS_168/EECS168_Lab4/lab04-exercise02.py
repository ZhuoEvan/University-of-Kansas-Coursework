'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/18/2024
Lab: lab04
Last modified: 02/18/2024
Purpose: List comparisons
'''
first = []
second = []

value_one = int(input('Enter a value for the first list: '))
first.append( value_one )
confirm_one = str(input('Are you done? (y|Y): '))
while confirm_one != 'y' and 'Y':
    value_one = int(input('Enter a value for the first list: '))
    first.append( value_one )
    confirm_one = str(input('Are you done? (y|Y): '))
print()
value_two = int(input('Enter a value for the second list: '))
second.append( value_two )
confirm_two = str(input('Are you done? (y|Y): '))
while confirm_two != 'y' and 'Y':
    value_two = int(input('Enter a value for the second list: '))
    second.append( value_two )
    confirm_two = str(input('Are you done? (y|Y): '))
print()
print('List statistics:')
old_num_one = 0
for num in first:
    first_total = num + old_num_one
    old_num_one = first_total
old_num_two = 0
for num in second:
    second_total = num + old_num_two
    old_num_two = second_total
if first_total > second_total:
    print('The first list has the larger sum of', first_total)
elif second_total > first_total:
    print('The second list has the larger sum of', second_total)
else:
    print('Both list have the same sum of', first_total)
v_first = 0
for num in first:
    v_first = v_first + 1
first_average = first_total / v_first
v_second = 0
for num in second:
    v_second = v_second + 1
second_average = second_total / v_first
if first_average > second_average:
    print('The first list has the larger average of', round(first_average, 1))
elif second_average > first_average:
    print('The second list has the larger average of', round(second_average, 1))
else:
    print('Both list have the same average of', round(first_average, 1))
appear = 0
for num_one in first:
    for num_two in second:
        if num_one == num_two:
            appear = appear + 1
print('Count of values that appear in both lists:', appear)
if first == second and first == second[::-1]:
    print('The lists are palindromes')
else:
    print('The lists are not palindromes')
