'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/7/2024
Lab: lab05
Last modified: 10/21/2024
Purpose: Blob Moving Maze Creator
'''
#mazemaker.py

from mazerunner import MazeRunner

class MazeMaker:
    def __init__(self, maze_map):
        #Initial Values
        self._maze_map = maze_map
        self._max_row = 0
        self._max_col = 0

    def run(self):
        #Opening the text file and extracting the content
        my_maze_stats = self.maze_stats(self._maze_map)
        maze_dimensions = my_maze_stats[0]
        #Error Check: Valid File Input
        if self.position_input_check(maze_dimensions) == False:
            raise ValueError('Only Row and Column')
        else:
            trace_map = self.trace_map_generation(int(maze_dimensions[0]), int(maze_dimensions[1]))
            blob_pos = my_maze_stats[1]
            #Error Check: Valid File Input
            if self.position_input_check(blob_pos) == False:
                raise ValueError('Only Blob_Start_Row and Blob_Start_Column')
            else:
                #Setting dimensions as a global variable
                #for an error check
                self._max_row = int(maze_dimensions[0])
                self._max_col = int(maze_dimensions[1])
                
                list_of_rows = []
                for row in range(2, len(my_maze_stats)):
                    for tile in my_maze_stats[row]:
                        list_of_rows.append(tile)
                generated_map = self.map_generation(list_of_rows)
                sewer_map = self.sewer(generated_map)
                
                #Run the MazeRunner Program
                my_mazerunner = MazeRunner(generated_map, trace_map, maze_dimensions, blob_pos, sewer_map)
                my_mazerunner.run()
                    
    def maze_stats(self, maze_file):
        #Opening the file and returning the content
        #in a readable way
        maze_stats = []
        with open(maze_file, 'r') as maze:
            for line in maze:
                clean_line = line.strip()
                split_line = clean_line.split(' ')
                maze_stats.append(split_line)
        return maze_stats

    def map_generation(self, tiles):
        #Splitting the map tiles into individual tiles
        #and returning a list of lists
        rows_columns = []
        for single_row in tiles:
            single_row_list = []
            for single_row_tile in single_row:
                single_row_list.append(single_row_tile)
            rows_columns.append(single_row_list)
        #Error Check: Generated Map matches Size
        if self.map_bound_check(rows_columns) == True:
            return rows_columns
        else:
            raise RuntimeError('Invalid Dimensions')

    def trace_map_generation(self, row, col):
        #Creating a mirror map with only '0' to trace the path
        #the blob goes
        trace_maze = []
        counter = row
        while counter != 0:
            trace_row = []
            for i in range(0, col):
                trace_row.append(0)
            trace_maze.append(trace_row)
            counter -= 1
        return trace_maze
        
    def position_input_check(self, positions):
        #Check if the first two lines only have two values
        if len(positions) == 2:
            return True
        else:
            return False

    def map_bound_check(self, tiles):
        #Error Check: Generated Map Rows matches Inputed Rows
        if len(tiles) != self._max_row:
            raise RuntimeError('Row Dimensions are Invalid')
        #Error Check: Generated Map Columns matches Inputed Columns
        for row in tiles:
            if len(row) != self._max_col:
                raise RuntimeError('Column Dimensions are Invalid')
        return True

    def sewer(self, tiles):
        #Scanning all tiles in the generated map to find '@'
        #and append the coordinates into a list of lists
        sewer_list = []
        for num1 in range(0, self._max_row):
            for num2 in range(0, self._max_col):
                if tiles[num1][num2] == '@':
                    sewer_coordinate = []
                    sewer_coordinate.append(num1)
                    sewer_coordinate.append(num2)
                    sewer_list.append(sewer_coordinate)
        return sewer_list
            
        
        
        
                
            
            
        
