FILE_NAME = 'day05.txt'

# similar approach at start to part 1

rules, updates = open(FILE_NAME, 'r').read().split('\n\n')
rules = rules.split('\n')
updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

rulesMap = {}
for rule in rules:
    a, b = rule.split('|')
    a, b = int(a.strip()), int(b.strip())
    if b not in rulesMap:
        rulesMap[b] = [a]
    else:
        rulesMap[b].append(a)

# function to check if broken
# return values that broken the rule


def broken(update):
    nums = set(update)
    seen = set()
    pair = []
    for n in update:
        broken = False
        if n in rulesMap:
            for p in rulesMap[n]:
                if p not in seen and p in nums:
                    broken = True
                    pair = [n, p]
                    break
        if broken:
            return pair

        seen.add(n)

    return False


# getting all incorrect updates
incorrect = []
for update in updates:
    if broken(update):
        incorrect.append(update)

# for every incorrect update
# swap the values that are broken until the rule is satisfied
# add the middle value to total
total = 0
for update in incorrect:
    while broken(update):
        pair = broken(update)
        update[update.index(pair[1])], update[update.index(
            pair[0])] = update[update.index(pair[0])], update[update.index(pair[1])]

    total += update[len(update)//2]

print(total)
