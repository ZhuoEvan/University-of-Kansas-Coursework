'''
Author: Evan Zhuo
KUID: 3109819
Date: 01/30/2024
Lab: lab02
Last modified: 01/30/2024
Purpose: Soda Packer
'''
soda = int(input("How many sodas do you have? "))
cubes = soda // 24
six = (soda % 24) // 6
single = cubes % 6
print(f'Fridge Cubes: {cubes}')
print(f'Six-packs: {six}')
print(f'Singles: {single}')
