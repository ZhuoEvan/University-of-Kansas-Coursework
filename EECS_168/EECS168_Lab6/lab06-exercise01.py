'''
Author: Evan Zhuo
KUID: 3109819
Date: 03/15/2024
Lab: lab06
Last modified: 03/15/2024
Purpose: Number Manipulation
'''
#Functions
def last_digit(num):
    ans = num % 10
    return ans

def remove_last_digit(num):
    ans = num // 10
    return ans

def add_digit(current_num, new_digit):
    extended_num = current_num * 10
    ans = extended_num + new_digit
    return ans

def reverse(num):
    ans = last_digit(num)
    num = remove_last_digit(num)
    while num != 0:
        reverse_num = last_digit(num)
        ans = add_digit(ans, reverse_num)
        num = remove_last_digit(num)
    return ans

def is_palindrome(num):
    palindrome_check = reverse(num)
    if num == palindrome_check:
        return True
    else:
        return False

def count_digits(num):
    ans = 0
    if num == 0:
        ans = 1
    while num !=0:
        num = remove_last_digit(num)
        ans += 1
    return ans

def sum_digits(num):
    ans = 0
    while num != 0:
        addition = last_digit(num)
        ans = ans + addition
        num = remove_last_digit(num)
    return ans

def print_menu():
    print('======= Menu =======')
    print('1) Count digits\n2) Sum digits\n3) Is Palindrome')
    print('4) Reverse\n5) Exit')
    print('====================')

def main():
    choice = 0
    while choice != 5:
        print_menu()
        choice = int(input('Choice: '))
        if choice >= 1 and choice <= 5:
            if choice >= 1 and choice < 5:
                num = int(input('Num: '))
                if choice == 1:
                    output = count_digits(num)
                    print('Output:',output,'\n')
                elif choice == 2:
                    output = sum_digits(num)
                    print('Output:',output,'\n')
                elif choice == 3:
                    output = is_palindrome(num)
                    print('Output:',output,'\n')
                else:
                    output = reverse(num)
                    print('Output:',output,'\n')
        else:
            print('Invalid Input\n')
    print('Exiting Program')
    
main()
