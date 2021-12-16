import math

lineData = open('lines.txt', 'r')

lines = list(map(lambda x: x[:-1], lineData.readlines()))

symbolMap = {
    ')': {
        'reverse': '(',
        'points': 1
    },
    '}': {
        'reverse': '{',
        'points': 3
    },
    ']': {
        'reverse': '[',
        'points': 2
    },
    '>': {
        'reverse': '<',
        'points': 4
    },
}

def revRevserve(symbol):
    for sym, mapping in symbolMap.items():
        if mapping['reverse'] == symbol:
            return sym

scores = []

for line in lines:
    total = 0
    corrupted = False
    symbols = []
    for symbol in line:
        if symbol in ['(', '[', '{', '<']:
            symbols.append(symbol)
        if symbol in [')', ']', '}', '>']:
            if symbolMap[symbol]['reverse'] == symbols[-1]:
                del symbols[-1]
            else:
                corrupted = True
                break
    if not corrupted:
        completeLine = []
        for symbol in symbols[::-1]:
            completeLine.append(revRevserve(symbol))
        for symbol in completeLine:
            total *=5
            total += symbolMap[symbol]['points']
        scores.append(total)

scores.sort()

print(scores[math.floor(len(scores)/2)])