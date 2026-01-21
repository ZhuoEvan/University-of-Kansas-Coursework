'''
Author: Evan Zhuo
KUID: 3109819
Date: 02/20/2024
Lab: lab05
Last modified: 02/25/2024
Purpose: Rook Path
'''
size = int(input('Size: '))
row_position = int(input('Rook Row: '))
row_position = row_position - 1
col_position = int(input('Rook Column: '))
col_position = col_position - 1
one_row = []
rook_row = []
board = []
horizontal = ''
for num in range(size):
    one_row.append('*')
for num in range(size):
    board.append(one_row)
for num in range(size):
    board[num][row_position] = '|'
for num in range(size):
    rook_row.append('-')
rook_row.pop(row_position)
rook_row.insert(row_position, 'R')
board.pop(col_position)
board.insert(col_position, rook_row)
for row in board:
        for space in row:
            print(space, end='')
        print()
