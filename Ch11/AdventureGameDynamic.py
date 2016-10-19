# Adventure game demo dynamic
import random

# Define some constants for items that will be found in the grid
EMPTY = 'e'
TREASURE = 't'
MONSTER = 'm'
SWORD = 's'
POTION = 'p'
addInToGrid = (TREASURE, TREASURE, TREASURE, MONSTER, MONSTER, MONSTER,\
               SWORD, SWORD, POTION, POTION)

NROWS_IN_GRID = 6
NCOLS_IN_GRID = 8 

# Find a random cell that is empty
def findEmptyCell(aGrid, nRows, nCols):
    while True:
        aRow = random.randrange(nRows)
        aCol = random.randrange(nCols)
        if aGrid[aRow][aCol] == EMPTY:
            return aRow, aCol


# Build grid, start it off all empty
grid = []
for r in range(0, NROWS_IN_GRID):
    aRow = []
    for c in range(0, NCOLS_IN_GRID):
        aRow.append(EMPTY)
    grid.append(aRow)

# Add in items randomly
for item in addInToGrid:
    locRow, locCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
    grid[locRow][locCol] = item

# For testing, print the grid, row by row
for thisRow in grid:
    print thisRow    

print
locRow, locCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
# For testing, print out the starting location so we know where we are in the grid
print 'Starting at  row:', locRow, '  col:', locCol

while True:  # play the game, move around the grid
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
    
    print
        
