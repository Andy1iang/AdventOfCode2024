import re

FILE_NAME = 'day03.txt'

line = open(FILE_NAME).read().strip()

# same approach as part 1
# but we split the line based on the 'do()' first, then split 'don't()'  to get the segments

total = 0

segments = [do.split('don\'t()')[0] for do in line.split('do()')]
for seg in segments:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, seg)
    for match in matches:
        total += int(match.split('(')[1].split(',')[0]) * int(match.split(',')[1].split(')')[0])

print(total)

