'''
Author: Evan Zhuo
KUID: 3109819
Date: 01/30/2024
Lab: lab02
Last modified: 01/30/2024
Purpose: Saffir-Simpson Scale
'''
wind = float(input("Input a wind speed (m/s): "))
if wind >= 70:
    print(f'A wind speed of {wind} is a Category 5 hurricane.')
elif wind >= 58:
    print(f'A wind speed of {wind} is a Category 4 hurricane.')
elif wind >= 50:
    print(f'A wind speed of {wind} is a Category 3 hurricane.')
elif wind >= 43:
    print(f'A wind speed of {wind} is a Category 2 hurricane.')
elif wind >= 33:
    print(f'A wind speed of {wind} is a Category 1 hurricane.')
elif wind >= 18:
    print(f'A wind speed of {wind} is a tropical storm.')
elif wind >= 0:
    print(f'A wind speed of {wind} is a tropical depression.')
else:
    print('Invalid wind speed')
