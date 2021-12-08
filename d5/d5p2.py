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
        for y in inclusiveRange(y1, y2, step):
            if (x1, y) not in coveredCoords:
                coveredCoords.add((x1, y))
            elif (x1, y) not in duplicate:
                duplicate.add((x1, y))
    elif y1 == y2:
        step = 1
        if x1 > x2:
            step = -1
        for x in inclusiveRange(x1, x2, step):
            if (x, y1) not in coveredCoords:
                coveredCoords.add((x, y1))
            elif (x, y1) not in duplicate:
                duplicate.add((x, y1))
    else:
        step = 1
        if y1 > y2:
            step = -1
        if x2 > x1:
            for x, y in enumerate(inclusiveRange(y1, y2, step), start=x1):
                if (x, y) not in coveredCoords:
                    coveredCoords.add((x, y))
                elif (x, y) not in duplicate:
                    duplicate.add((x, y))
        else:
            for x, y in enumerate(inclusiveRange(y1, y2, step)[::-1], start=x2):
                if (x, y) not in coveredCoords:
                    coveredCoords.add((x, y))
                elif (x, y) not in duplicate:
                    duplicate.add((x, y))

print(len(duplicate))