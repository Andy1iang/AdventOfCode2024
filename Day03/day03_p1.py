import re

FILE_NAME = 'day03.txt'

line = open(FILE_NAME).read().strip()

# regex pattern to match
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, line)

# calculating the total product
total = 0
for match in matches:
    total += int(match.split('(')[1].split(',')[0]) * \
        int(match.split(',')[1].split(')')[0])

print(total)
