ventData = open('vent.txt', 'r')

ventCoords = list(map(lambda x: x[:-1].replace(' ->', '').split(' '), ventData.readlines()))

for i, coords in enumerate(ventCoords):
    ventCoords[i] = tuple(map(lambda x: x.split(','), coords))

def inclusiveRange(start, stop, step):
    return range(start, (stop + 1) if step >= 0 else (stop - 1), step)

coveredCoords = set()

duplicate = set()

for coords in ventCoords:
    x1 = int(coords[0][0])
    x2 = int(coords[1][0])
    y1 = int(coords[0][1])
    y2 = int(coords[1][1])
    if x1 == x2:
        step = 1
        if y1 > y2:
            step = -1
        for i in inclusiveRange(y1, y2, step):
            if (x1, i) not in coveredCoords:
                coveredCoords.add((x1, i))
            elif (x1, i) not in duplicate:
                duplicate.add((x1, i))
    elif y1 == y2:
        step = 1
        if x1 > x2:
            step = -1
        for i in inclusiveRange(x1, x2, step):
            if (i, y1) not in coveredCoords:
                coveredCoords.add((i, y1))
            elif (i, y1) not in duplicate:
                duplicate.add((i, y1))
    

print(len(duplicate))