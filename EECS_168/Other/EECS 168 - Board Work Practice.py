'''
EECS 168
Programming I
Board Work Practice Document
7 May 2024
'''

#Board Work 1
'''
animal = input('Enter an animal: ')
print(f'{animal} is super adorable!')
'''

#Board Work 2
'''
base = float(input('Enter a triangle base: '))
height = float(input('Enter a triangle height: '))
area = 0.5*base*height
print(area)
'''

#Board Work 3
'''
grade = float(input('Quiz Score: '))
if grade >= 100:
    print('A+')
if grade >= 89 and grade < 100:
    print('A')
if grade >= 79 and grade < 89:
    print('B')
if grade >= 69 and grade < 79:
    print('C')
if grade >= 59 and grade < 69:
    print('D')
if grade >= 0 and grade < 59:
    print('F')
if grade < 0:
    print('Invalid Grade')
'''

#Board Work 4
'''
for num in range(1, 101):
    print(num)
for num in range(100, -101, -1):
    print(num)
for num in range(6, 667, 6):
    print(num)
for num in range(1, 1001):
    print('A')
guess = 'x'
while guess != 'q':
    guess = input('Enter a letter: ')
    guess = guess.lower()
'''

#Board Work 5
'''
username = input('Enter a username: ')
if 'jwg' in username[0]+username[1]+username[2]:
    password = input('Enter a password: ')
    if '!' in password:
        if '@' in password:
            print('welcome')
        else:
            print('failure')
    else:
        print('failure')
else:
    print('failure')
'''

#Board Work 10
'''
def main():
    judge = input('Enter a string: ')
    result = judgement(judge)
    print(result)
def judgement(string):
    if len(string) >= 5 and len(string) <= 10:
        return True
    else:
        return False
main()
'''

#Board Work 12
'''
def main():
    w = input('Word: ')
    n = int(input('Times: '))
    mult_print(w, n)
def mult_print(word, num):
    for _ in range(0, num):
        print(word + '!')
main()
'''

#Board Work 13
'''
my_dict = {}
string = str(input('Enter a string: '))
for letter in string:
    my_dict[letter] = string.count(letter)
print(my_dict)
'''

#Board Work 14
'''
import random
def main():
    my_lotto = []
    for num in range(1,7):
        lotto = int(input('Enter Lotto Number: '))
        my_lotto.append(lotto)
    board = lottoroll()
    if sorted(my_lotto) == sorted(board) :
        print('Win')
    else:
        print('Loss')
        print(board)
        
def lottoroll():
    for num in range(1,7):
        roll = random.sample(range(1,37),k=6)
    return roll
main()
'''

#Board Work 15
'''
a168 = input('Enter 168 IDs: ')
a140 = input('Enter 140 IDs: ')
delimiter = ','
s168 = a168.split(delimiter)
s140 = a140.split(delimiter)
for student in s168:
    if student in s140:
        pass
    else:
        print(f'Only in 168: {student}')
for student in s168:
    if student in s140:
        print(f'In both 140 and 168: {student}')
    else:
        pass
'''

#Board Work 16
'''
def main():
    my_list = [2, 3, 4, 5, 10, 24]
    print(double(my_list))
    print(odd(my_list))
def double(numlist):
    doublelist = []
    for num in numlist:
        double = num*2
        doublelist.append(double)
    return doublelist
def odd(numlist):
    oddlist = []
    for num in numlist:
        if num%2!=0:
            oddlist.append(num)
    return oddlist
main()
'''

#Board Work 22
'''
from cylinder import Cylinder
import random
def main():
    my_cylinder = Cylinder()
    cylinderlist = []
    for num in range(1, 1224):
        my_cylinder.radius = random.randint(1, 100)
        my_cylinder.height = random.randint(1, 100)
        cylinderlist.append(my_cylinder.volume(my_cylinder.radius, my_cylinder.height))
    for cylinder in cylinderlist:
        print(cylinder)
main()
'''

#Board Work 23
'''
gate = False
while gate == False:
    try:
        age = int(input('Enter a valid age: '))
        if age <= 0:
            raise ZeroDivisionError
        print(age)
        gate = True
    except ValueError:
        print('What is your age, really')
    except ZeroDivisionError:
        print('Quit the cap, what is your real age?')
'''

#Board Work 24
'''
def main():
    gate = False
    while gate == False:
        try:
            top = int(input('Numerator: '))
            bot = int(input('Denominator: '))
            fraction = my_div(top, bot)
            print(fraction)
            gate = True
        except ValueError:
            print('You idiot! A NUMBER!!!')
            gate = False
        except ZeroDivisionError:
            print('You FOOL! NO ZERO DENOMINATOR!!!')
            gate = False
def my_div(numerator, denominator):
    fraction = numerator/denominator
    return fraction
main()
'''

#Board Work 25
'''
nums = [3, 5, 15, 2, 9, 7, 30]
fizzbuzzmaker = ['fizzbuzz' if num%3==0 and num%5==0 else 'fizz' if num%3==0 else 'buzz' for num in nums if num%3 == 0 or num%5 == 0]
print(fizzbuzzmaker)
'''
