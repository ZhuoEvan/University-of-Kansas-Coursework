'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/7/2024
Lab: lab05
Last modified: 10/21/2024
Purpose: Blob Moving Start
'''
#main.py

from mazemaker import MazeMaker

def main():
    #Receive text file from user
    maze_file = input("Enter the name of the input file: ")
    my_maze = MazeMaker(maze_file)
    my_maze.run()

if __name__ == "__main__":
    main()
