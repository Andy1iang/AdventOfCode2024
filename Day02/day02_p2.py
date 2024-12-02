FILE_NAME = 'day02.txt'

lines = [list(map(int, line.strip().split()))
         for line in open(FILE_NAME).readlines()]

total = 0

# same approach as part 1
# but now we check the line and all possibilities of removing one element

for line in lines:
    permutations = []
    permutations.append(line)
    for i in range(len(line)):
        permutations.append(line[:i] + line[i+1:])

    for perm in permutations:
        inc = True
        for i in range(1, len(perm)):
            if i == 1:
                inc = True if perm[i] > perm[i-1] else False
            if (inc and perm[i] <= perm[i-1]) or (not inc and perm[i] >= perm[i-1]) or (abs(perm[i] - perm[i-1]) > 3):
                break

        else:
            total += 1
            break

print(total)
