FILE_NAME = 'day01.txt'

lines = [line.strip() for line in open(FILE_NAME).readlines()]

# split the numbers into two lists (sorted)
lst1 = []
lst2 = []
for line in lines:
    lst1.append(int(line.split()[0]))
    lst2.append(int(line.split()[1]))
lst1.sort()
lst2.sort()

# calculate the total difference between the two lists
total = 0
for i in range(len(lst1)):
    total += abs(lst2[i] - lst1[i])

print(total)
