'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/23/2024
Lab: lab02
Last modified: 9/25/2024
Purpose: CPU Scheduler Start
'''
#start.py

from cpu_scheduler import CPU_Scheduler

def main():
    command_list = input('Enter the command file name: ')
    my_cpu = CPU_Scheduler(command_list)
    my_cpu.run()

if __name__ == "__main__":
    main()
