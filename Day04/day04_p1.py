FILE_NAME = 'day04.txt'

grid = [list(line.strip()) for line in open(FILE_NAME).readlines()]

# function to check how many XMAS are in the grid


def check(row, col):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total = 0
    # for each direction, check if there is an M, A, and S in the next
    for dr, dc in dirs:
        if dr*3 + row < 0 or dr*3 + row >= len(grid) or dc*3 + col < 0 or dc*3 + col >= len(grid[row]):
            continue
        if grid[dr + row][dc + col] == 'M' and grid[dr*2 + row][dc*2 + col] == 'A' and grid[dr*3 + row][dc*3 + col] == 'S':
            total += 1
    return total


# count the total number of XMAS in the grid
total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'X':
            total += check(row, col)

print(total)
