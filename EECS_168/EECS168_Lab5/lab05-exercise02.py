'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/20/2024
Lab: lab05
Last modified: 02/26/2024
Purpose: Numeric File Analysis
'''
#Opening input.txt
start_file = open('input.txt', 'r')
data = start_file.read()
start_list = []
data_list = []
start_list.append(data)
start_list = data.split('\n')
for row in start_list:
    new_row = row.split(' ')
    data_list.append(new_row)
row = int(data_list[0][0])
col = int(data_list[0][1])
#Writing averages.txt
ave = open('averages.txt', 'w')
delimiter = ' '
ave_div = 0
total_average = 0
old_digit = 0
for num in range(1, len(data_list)):
    value = data_list[num]
    for digit in value:
        ave_div += 1
for num in range(1, len(data_list)):
    value = data_list[num]
    for digit in value:
        total_average = float(digit) + float(old_digit)
        old_digit = float(total_average)
    ave_total = float(total_average) / float(ave_div)
ave.write('Total average: ')
ave.write(str(ave_total))
ave.write('\n')
average_list = []
for num in range(1, len(data_list)):
    average = 0
    div = 0
    old_digit = 0
    value = data_list[num]
    for digit in value:
        average = float(digit) + float(old_digit)
        old_digit = float(average)
    row_ave = float(average) / float(len(value))
    average_list.append(str(row_ave))
for num in range(0, len(data_list) - 1):
    average = average_list[num]
    ave.write('Row ')
    ave.write(str(num + 1))
    ave.write(' average: ')
    ave.write(str(average))
    ave.write('\n')
ave.close()
#Writing reverse.txt
rev = open('reverse.txt', 'w')
delimiter = ' '
for num in range(1, len(data_list)):
    value = data_list[num]
    value.reverse()
    write_value = delimiter.join(value)
    rev.write(write_value)
    rev.write('\n')
rev.close()
#Writing flipped.txt
fli = open('flipped.txt', 'w')
delimiter = ' '
data_list.reverse()
for num in range(0, len(data_list) - 1):
    value = data_list[num]
    value.reverse()
    write_value = delimiter.join(value)
    fli.write(write_value)
    fli.write('\n')
fli.close()
data_list.reverse()
#Writing diagonal.txt
if row == col:
    dia = open('diagonal.txt', 'w')
    delimiter = ' '
    total_value = []
    for digit in range(0, len(data_list) - 1):
        dia_value = []
        for num in range(1, len(data_list)):
            value = data_list[num][digit]
            dia_value.append(value)
        total_value.append(dia_value)
    for value in total_value:
        write_value = delimiter.join(value)
        dia.write(write_value)
        dia.write('\n')
    dia.close()
#Writing transpose.txt
tra = open('transpose.txt', 'w')
delimiter = ' '
total_value = []
for a_row in range(0, row):
    tra_value = []
    for a_col in range(1, col + 1):
        value = data_list[a_col][a_row]
        tra_value.append(value)
    total_value.append(tra_value)
for value in total_value:
    write_value = delimiter.join(value)
    tra.write(write_value)
    tra.write('\n')
tra.close()
start_file.close()

