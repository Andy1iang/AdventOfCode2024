FILE_NAME = 'day02.txt'

lines = [list(map(int, line.strip().split()))
         for line in open(FILE_NAME).readlines()]

total = 0

# for each line, check if the difference between the current and previous number is greater than 3
# also check if all of them are in increasing or decreasing order (by checking the first one)
for line in lines:
    inc = True
    for i in range(1, len(line)):
        if i == 1:
            inc = True if line[i] > line[i-1] else False
        if (inc and line[i] <= line[i-1]) or (not inc and line[i] >= line[i-1]) or (abs(line[i] - line[i-1]) > 3):
            break

    # if valid, add one to the total
    else:
        total += 1

print(total)
