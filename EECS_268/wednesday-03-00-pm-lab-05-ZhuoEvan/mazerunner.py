'''
Author: Evan Zhuo
KUID: 3109819
Date: 10/7/2024
Lab: lab05
Last modified: 10/21/2024
Purpose: Blob Moving Maze Solver
'''
#mazerunner.py

class MazeRunner:
    def __init__(self, maze_map, trace_maze, dimensions, blob_pos, sewer_coords):
        #Initial Values
        self._maze_map = maze_map
        self._trace_maze = trace_maze
        self._max_row = int(dimensions[0])
        self._max_col = int(dimensions[1])
        self._blob_row = int(blob_pos[0])
        self._blob_col = int(blob_pos[1])
        self._sewer_coords = sewer_coords
        self._trace_count = 0
        self._people_eaten = 0

    def run(self):
        #Start the blob maze
        #Error Check: Valid Blob Position
        if self.walk(self._blob_row, self._blob_col) == True:
            #Print the map status
            for tile in self._maze_map:
                print(tile)
            #Return the people eaten stats
            print(f'\nTotal eaten: {self._people_eaten}')
        else:
            raise RuntimeError('Invalid Starting Tile')
            
    def walk(self, row, col):
        #Error Check: Valid Starting Tile
        if self.is_valid_move(row, col) == False:
            return False
        else:
            #Special Tile Functions
            self.special_tile(row, col)
            #Mark Tile
            current_tile = self._maze_map[row][col]
            if current_tile != '@':
                self.mark(row, col)
            #Look North
            if self.is_valid_move(row - 1, col) == True:
                self.walk(row - 1, col)
            #Look East
            if self.is_valid_move(row, col + 1) == True:
                self.walk(row, col + 1)
            #Look South
            if self.is_valid_move(row + 1, col) == True:
                self.walk(row + 1, col)
            #Look West
            if self.is_valid_move(row, col - 1) == True:
                self.walk(row, col - 1)
            #All Four Directions of Starting Tile has been Checked
            return True

    def mark(self, row, col):
        #Set the Tile as 'B'
        self._maze_map[row][col] = 'B'
        #Set the Current Tile as Trace Count on Trace Map
        self._trace_count += 1
        self._trace_maze[row][col] = self._trace_count

    def special_tile(self, row, col):
        #Special Tile will enact their function
        tile = self._maze_map[row][col]
        if tile == 'P':
            self.add_people()
        if tile == '@':
            self._trace_count += 1
            self._trace_maze[row][col] = self._trace_count
            for sewer in self._sewer_coords:
                if self._trace_maze[sewer[0]][sewer[1]] == 0:
                    self.walk(sewer[0], sewer[1])
        else:
            return

    def is_valid_move(self, row, col):
        #Check if tile is within the bounds and is a valid space
        if self.in_bound(row, col) == False:
            return False
        elif self.tile_reader(row, col) == False:
            return False
        else:
            return True

    def in_bound(self, row, col):
        #Check location with bounds of maze
        if row < 0 or row > self._max_row - 1:
            return False
        elif col < 0 or col > self._max_col - 1:
            return False
        else:
            return True

    def tile_reader(self, row, col):
        #Getting the current Tile and Marking Tile
        tile = self._maze_map[row][col]
        mark_tile = self._trace_maze[row][col]
        
        #Building Tile
        if tile == '#':
            return False
        #Streets and People Tiles
        elif tile == 'S' or tile == 'P':
            return True
        #Marked Tile
        elif mark_tile != 0:
            return False
        #Sewer Tile
        elif tile == '@':
            return True
        #Error Check: Invalid Tile
        else:
            raise RuntimeError('Invalid tile_type')

    def add_people(self):
        #Add people to the people_eaten counter
        self._people_eaten += 1
