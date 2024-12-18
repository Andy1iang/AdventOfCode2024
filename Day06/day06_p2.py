FILE_NAME = 'day06.txt'

grid = [list(line.strip()) for line in open(FILE_NAME).readlines()]

# finding the starting point
coord = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            coord = [i, j]

# starting parameters
startI, startJ = coord
startDirection = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# function to check if there is a loop


def loop(grid, i, j, direction):
    seen = set()
    seen.add((i, j, direction))
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        if grid[i][j] == '#':
            i, j = i - directions[direction][0], j - directions[direction][1]
            direction = (direction + 1) % 4
            i, j = i + directions[direction][0], j + directions[direction][1]

        else:
            i, j = i + directions[direction][0], j + directions[direction][1]

        if (i, j, direction) in seen:
            break
        seen.add((i, j, direction))
    else:
        return False

    return True

# finding all path we take from the starting point


def findPath(grid, i, j, direction):
    points = set()
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        if grid[i][j] != "#":
            points.add((i, j))

        if grid[i][j] == '#':
            i, j = i - directions[direction][0], j - directions[direction][1]
            direction = (direction + 1) % 4
            i, j = i + directions[direction][0], j + directions[direction][1]

        else:
            i, j = i + directions[direction][0], j + directions[direction][1]

    return points


# getting all points on the path except the start
points = findPath(grid, startI, startJ, startDirection)
points.remove((startI, startJ))

# checking if there is a loop for each point
total = 0
for point in points:
    grid[point[0]][point[1]] = '#'
    if loop(grid, startI, startJ, startDirection):
        total += 1
    grid[point[0]][point[1]] = '.'

print(total)
