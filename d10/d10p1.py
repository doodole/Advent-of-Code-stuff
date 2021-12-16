lineData = open('lines.txt', 'r')

lines = list(map(lambda x: x[:-1], lineData.readlines()))

symbolMap = {
    ')': {
        'reverse': '(',
        'points': 3
    },
    '}': {
        'reverse': '{',
        'points': 1197
    },
    ']': {
        'reverse': '[',
        'points': 57
    },
    '>': {
        'reverse': '<',
        'points': 25137
    },
}

total = 0

for line in lines:
    symbols = []
    for symbol in line:
        if symbol in ['(', '[', '{', '<']:
            symbols.append(symbol)
        if symbol in [')', ']', '}', '>']:
            if symbolMap[symbol]['reverse'] == symbols[-1]:
                del symbols[-1]
            else:
                total += symbolMap[symbol]['points']
                break
print(total)