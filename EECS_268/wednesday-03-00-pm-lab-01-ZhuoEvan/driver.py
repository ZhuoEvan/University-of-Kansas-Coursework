'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/11/2024
Lab: lab01
Last modified: 9/15/2024
Purpose: Board Game Start
'''
#driver.py

from executive import Executive

def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.run()

if __name__ == "__main__":
  main()
