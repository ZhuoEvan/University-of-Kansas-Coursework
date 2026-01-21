'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/30/2024
Lab: lab04
Last modified: 10/4/2024
Purpose: Outbreak Recursion Exercise
'''
#exercise2.py

def main():
    #Error Check: Valid Inputs
    error_check_gate = False
    while error_check_gate == False:
        #try-except block will repeat until given valid inputs
        try:
            print('OUTBREAK!')
            day = int(input('What day do you want a sick count for?: '))
            #Error Check: Day less than or equal to Zero
            if day <= 0:
                raise RuntimeError
            else:
                error_check_gate = True
                
        #Except block returns invalid day
        except:
            print('Invalid day\n')

    #Send the day input into outbreak function
    outbreak_result = outbreak(day)
    print(outbreak_result)
            
#Outbreak Function
def outbreak(day):
    #Day 1 Output
    if day == 1:
        return 6
    #Day 2 Output
    elif day == 2:
        return 20
    #Day 3 Output
    elif day == 3:
        return 75
    #Day 4 and up Output
    else:
        flu = outbreak(day - 1) + outbreak(day - 2) + outbreak(day - 3)
        return flu

main()
