FILE_NAME = 'day05.txt'

# getting rules and updates
rules, updates = open(FILE_NAME, 'r').read().split('\n\n')
rules = rules.split('\n')
updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

# second element as the key and the first as the value (stored in a list in case of multiple values)
rulesMap = {}
for rule in rules:
    a, b = rule.split('|')
    a, b = int(a.strip()), int(b.strip())
    if b not in rulesMap:
        rulesMap[b] = [a]
    else:
        rulesMap[b].append(a)

# checking if the update is broken
total = 0
for update in updates:
    nums = set(update)  # set of all elements in the update
    seen = set()  # set of elements that have been seen
    for n in update:
        # broken if value is in nums but not in seen (does not precede key)
        broken = False
        if n in rulesMap:
            for p in rulesMap[n]:
                if p not in seen and p in nums:
                    broken = True
                    break
        if broken:
            break

        seen.add(n)

    # if not broken, get middle elements
    else:
        total += update[len(update)//2]

print(total)
