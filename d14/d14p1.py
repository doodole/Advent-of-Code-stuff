polymerData = open('polymer.txt', 'r') 

polymerData = list(map(lambda x: x[:-1], polymerData.readlines()))

polymerTemplate = list(polymerData[0])

polymerInsertionRules = {}

for rule in polymerData[2:]:
    polymerInsertionRules[rule[0:2]] = rule[-1]

newChain = []

steps = 10

for _ in range(steps):
    newChain = []

    for i, polymer in enumerate(polymerTemplate[:-1]):
        pair = polymer + polymerTemplate[i + 1]
        if pair in polymerInsertionRules:
            newChain.extend(polymer + polymerInsertionRules[pair])


    newChain.append(polymerTemplate[-1])

    polymerTemplate = newChain

max = -1
min = 573409587

for polymer in set(polymerTemplate):
    count = polymerTemplate.count(polymer)
    if count > max:
        max = count
    if count < min:
        min = count

print(max - min)
