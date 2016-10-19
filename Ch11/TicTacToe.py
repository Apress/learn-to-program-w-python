EMPTY = ''
X = 'x'
O = 'o'

# Build a 3 by 3 grid
grid = [\
          [EMPTY, EMPTY, EMPTY],\
          [EMPTY, EMPTY, EMPTY],\
          [EMPTY, EMPTY, EMPTY]\
          ]

print grid

row = 0
col = 2
grid[row][col] = X

print grid

for row in grid:
    print row
