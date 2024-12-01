FILE_NAME = 'day01.txt'

lines = [line.strip() for line in open(FILE_NAME).readlines()]

# lst 1 is a list of all the numbers on the left
# lst 2 is a dictionary of all the numbers on the right and their frequency
lst1 = []
lst2 = {}
for line in lines:
    l, r = line.split()
    l, r = int(l), int(r)
    lst1.append(l)
    if r not in lst2:
        lst2[r] = 1
    else:
        lst2[r] += 1

# iterate through lst1 and check if the number is in lst2
# if it is, add the product of the number and the frequency to the total
total = 0
for num in lst1:
    if num in lst2:
        total += lst2[num] * num

print(total)
