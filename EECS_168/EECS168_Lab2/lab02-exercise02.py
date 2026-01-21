'''
Author: Evan Zhuo
KUID: 3109819
Date: 01/30/2024
Lab: lab02
Last modified: 01/30/2024
Purpose: Long Division Printer
'''
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))
integer = numerator // denominator
remainder = numerator % denominator
print(f'{numerator} / {denominator} = {integer} Remainder {remainder}')
