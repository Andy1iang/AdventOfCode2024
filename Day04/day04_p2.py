FILE_NAME = 'day04.txt'

grid = [list(line.strip()) for line in open(FILE_NAME).readlines()]

# similar approach to part 1, but only 1 MAS is possible per A


def check(row, col):
    # left up, left down, right up, right down
    lu, ld, ru, rd = (-1 + row, -1 + col), (1 + row, -1 +
                                            col), (-1 + row, 1 + col), (1 + row, 1 + col)

    # checking for index out of bounds
    if lu[0] < 0 or lu[1] < 0 or rd[0] >= len(grid) or rd[1] >= len(grid[row]):
        return 0

    # checking for M and S (2 each)
    letters = grid[lu[0]][lu[1]] + grid[ld[0]][ld[1]] + \
        grid[ru[0]][ru[1]] + grid[rd[0]][rd[1]]
    if letters.count('M') == 2 and letters.count('S') == 2:
        # checking for M in diagonals (not supposed to be)
        if grid[lu[0]][lu[1]] == 'M' and grid[rd[0]][rd[1]] == 'M':
            return 0
        if grid[ld[0]][ld[1]] == 'M' and grid[ru[0]][ru[1]] == 'M':
            return 0
        return 1

    return 0


# getting total
total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'A':
            total += check(row, col)

print(total)
