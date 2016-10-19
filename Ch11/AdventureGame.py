#  Adventure game demo
import random

EMPTY = 'e'
TREASURE = 't'
MONSTER = 'm'

# Build 6 by 6 grid
NROWS_IN_GRID = 6
NCOLS_IN_GRID = 6 
grid = [\
          [EMPTY, TREASURE, EMPTY, EMPTY, EMPTY, MONSTER],\
          [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],\
          [EMPTY, EMPTY, EMPTY, EMPTY, MONSTER, EMPTY],\
          [EMPTY, MONSTER, EMPTY, EMPTY, EMPTY, EMPTY],\
          [EMPTY, EMPTY, EMPTY, EMPTY, TREASURE, EMPTY],\
          [EMPTY, TREASURE, EMPTY, EMPTY, EMPTY, EMPTY],\
          ]

# Find a random starting cell that is empty
while True:
    locRow = random.randrange(NROWS_IN_GRID)
    locCol = random.randrange(NCOLS_IN_GRID)
    if grid[locRow][locCol] == EMPTY:
        break   # found an empty cell, we will place the player here

print 'Starting at  row:', locRow, '  col:', locCol
print

while True:  # move around the grid
    direction = raw_input('Press L, U, R, or D to move: ')
    direction = direction.lower()
    print
    
    if direction == 'l':
        locCol = locCol - 1
        
    elif direction == 'u':
        locRow = locRow - 1
        
    elif direction == 'r':
        locCol = locCol + 1
        
    elif direction == 'd':
        locRow = locRow + 1

    else:
        print 'Oops - staying where we are ... '

    foundInCell = grid[locRow][locCol]
    print 'Now at row:', locRow, '   col:', locCol, '    cell contains:', foundInCell

    # Add code here to do whatever you want with the contents of the current cell
    #  (e.g., fight, run, pick up, etc.)

        
