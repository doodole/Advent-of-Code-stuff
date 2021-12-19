polymerData = open('polymer.txt', 'r') 

polymerData = list(map(lambda x: x[:-1], polymerData.readlines()))

polymerTemplate = list(polymerData[0])

polymerPairs = {}

polymerInsertionRules = {}

for rule in polymerData[2:]:
    polymerInsertionRules[rule[0:2]] = rule[-1]
    polymerPairs[rule[0:2]] = 0

for i, polymer in enumerate(polymerTemplate[:-1]):
    pair = polymer + polymerTemplate[i + 1]
    polymerPairs[pair] +=1

steps = 40

polymerCounts = {}
for polymer in polymerTemplate:
    if polymer in polymerCounts:
        polymerCounts[polymer] += 1
    else:
        polymerCounts[polymer] = 1

for _ in range(steps):
    newPolymer = {}
    for rule in polymerData[2:]:
        newPolymer[rule[0:2]] = 0
    
    for pair, count in polymerPairs.items():
        insertion = polymerInsertionRules[pair]
        if insertion in polymerCounts:
            polymerCounts[insertion] += count
        else:
            polymerCounts[insertion] = count
        newPolymer[insertion + pair[1]] += count
        newPolymer[pair[0] + insertion] += count
    
    polymerPairs = newPolymer

min = 34054309528340928503948609348053480534805830426534250324
max = -1

for polymer, count in polymerCounts.items():
    if count > max:
        max = count
    if count < min:
        min = count


print(max - min, max, min)