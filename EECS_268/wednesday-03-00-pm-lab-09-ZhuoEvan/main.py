'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/30/2024
Lab: lab09
Last modified: 12/03/2024
Purpose: Timing Main
'''
#main.py

#Import Modules
import time
import random
from operationtimer import OperationTimer

#Main Function
def main():
    #Initial Variables
    quit_gate = 0

    while quit_gate == 0:
        try:
            #User Input
            print(select_menu())
            user_input = int(input('Enter a Number: '))
            print('\n')

            #Error Check: Valid Input
            if user_input < 1 or user_input > 8:
                raise RuntimeError
            
            #Exit Option
            elif user_input == 8:
                quit_gate = 1

            #Time an Operation Option
            else:
                #Initial Variables
                end_time_ns = []
                end_time_sec = []
                element_amount = 1000
                percent = 0

                #Time Operation until element_amount reaches 100000
                while element_amount != 101000:
                    #Loading Function
                    percent += 1
                    print('{{',f'Loading Status: {percent}%','}}')

                    #Set-up Operation
                    my_operation = pre_action(element_amount, user_input)
                    #Start Timer for Operation Action
                    start = timer_run()
                    function_run(user_input, my_operation)
                    timer_stop(end_time_ns, end_time_sec, start)
                    #Repeat Operation with 1000 More Elements Added
                    element_amount += 1000

                #Allow User to Read Times
                print(f'Average time in ns: {average_time(end_time_ns)}')
                print(f'Average time in sec: {average_time(end_time_sec)}')
                input('{{Press Enter to Return Back to Menu}}')

        #Error Message
        except RuntimeError:
            print('{{Invalid Input: Integer Out of Bounds}}\n')
        except:
            print('{{Invalid Input: Not an Integer}}\n')

    #Program Exit
    print('{{Exiting the Program...}}')

#Random Number List Maker
def random_maker(element_amount):
    random_list = set()
    while len(random_list) != element_amount:
        random_list.add(random.randint(0, 999999)) #All integers are unique
    return random_list

#Pre Timer Function
def pre_action(element_amount, setting):
    elements = random_maker(element_amount)
    #Preload Data Structure Switch
    #Preload Stack
    if setting == 1 or setting == 2:
        my_operation = OperationTimer(elements, 0)
    #Preload LinkedList
    elif setting == 4 or setting == 5:
        my_operation = OperationTimer(elements, 1)
    #Preload MaxHeap
    elif setting == 6:
        my_operation = OperationTimer(elements, 2)
    #Preload Binary Search Tree
    elif setting == 7:
        my_operation = OperationTimer(elements, 3)
    #No Preload
    else:
        my_operation = OperationTimer(elements, 4)
    return my_operation

#Timer Start Function
def timer_run():
    print("Beginning the timing code...")
    start_time = time.process_time_ns()
    return start_time

#Operation Run Function
def function_run(select, code_operation):
    #Time: Pop a Single Item in a Stack
    if select == 1:
        while code_operation.single_stack() is False:
            pass
    #Time: Pop All Items in a Stack
    elif select == 2:
        while code_operation.all_stack() is False:
            pass 
    #Time: Enqueue All Items in a LinkedQueue
    elif select == 3:
        while code_operation.queue_enqueue() is False:
            pass
    #Time: get_entry at Last Entry in a LinkedList
    elif select == 4:
        while code_operation.linkedlist_last_entry() is False:
            pass
    #Time: get_entry All Items in a LinkedList
    elif select == 5:
        while code_operation.linkedlist_all_entry() is False:
            pass
    #Time: Add Value to a MaxHeap
    elif select == 6:
        while code_operation.maxheap_add() is False:
            pass 
    #Time: Search For A Value in a Binary Search Tree
    else:
        while code_operation.binarytree_search() is False:
            pass
    
    #Function Completed
    return

#Timer Stop Function
def timer_stop(end_time_ns, end_time_sec, start_time):
    end_time = time.process_time_ns()

    #Print The Total Time in ns and sec
    print("Total time in ns: ", end_time - start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time - start_time))

    #Append Total Time to Both Lists to Create Average Times
    end_time_ns.append(end_time - start_time)
    end_time_sec.append(nanosec_to_sec(end_time - start_time))
    print('\n')
    #Return Both Average Time Lists
    return end_time_ns, end_time_sec

#Seconds Converter Function
def nanosec_to_sec(ns):
    billion = 1000000000
    return ns/billion

#Average Time Function
def average_time(times_list):
    #Initial Variables
    sum = 0

    #Adding All Times Together
    for num in times_list:
        sum = sum + num
    #Dividing Sum by Number of Times
    average_time = sum/len(times_list)
    #Return Average Time
    return average_time

#Selection Menu Function
def select_menu():
    menu = '================================================'
    menu += '\n Please Select an Operation to Time:\n'
    menu += '1) Pop a Single Item in a Stack\n2) Pop All Items in a Stack\n'
    menu += '3) Enqueue All Items in a LinkedQueue\n4) get_entry at Last Entry in a LinkedList\n'
    menu += '5) get_entry All Items in a LinkedList\n6) Add Value to a MaxHeap\n'
    menu += '7) Search For A Value in a Binary Search Tree\n8) Exit\n'
    menu += '================================================'
    return menu

main()