FILE_NAME = 'day06.txt'

grid = [list(line.strip()) for line in open(FILE_NAME).readlines()]

# finding the starting point
coord = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            coord = [i, j]

# to turn right when we need
i, j = coord
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0

# turn right when we hit '#' obstacle
# mark grid point as 'X' when it's not an obstacle
# keeping going until we go out of bounds
while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
    if grid[i][j] == '#':
        i, j = i - directions[direction][0], j - directions[direction][1]
        direction = (direction + 1) % 4
        i, j = i + directions[direction][0], j + directions[direction][1]

    else:
        grid[i][j] = 'X'
        i, j = i + directions[direction][0], j + directions[direction][1]

# count the total number of 'X' in the grid
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            total += 1

print(total)
