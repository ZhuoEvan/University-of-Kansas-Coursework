'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/09/2024
Lab: lab03
Last modified: 02/12/2024
Purpose: Outbreak!
'''
print('OUTBREAK!')
day = int(input('What day do you want a sick count for?: '))
flu = 0
if day == 1:
    flu = 1
elif day == 2:
    flu = 4
elif day == 3:
    flu = 64
elif day >= 4:
    previous_day = 0
    day_one = 1
    day_two = 4
    day_three = 64
    flu_count = 0
    for num in range(4, day + 1):
        flu_count = day_one + day_two + day_three
        day_one = day_two
        day_two = day_three
        day_three = flu_count
    flu = flu_count
else:
    print('Invalid day')
if day > 0:
    print('Total people with flu:', flu)
