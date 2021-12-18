dotsData = open('dots.txt', 'r')

dotsData = list(map(lambda x: x[:-1], dotsData.readlines()))

linebreak = dotsData.index('')

dotCoords = list(map(lambda x: tuple(map(int, x.split(','))), dotsData[:linebreak]))

folds = list(map(lambda x: x.split(' ')[-1], dotsData[linebreak + 1:]))

for fold in folds:
    for i, coord in enumerate(dotCoords):
        if fold[0] == 'x':
            xFold = int(fold[2:])
            if coord[0] > xFold:
                dotCoords[i] = (xFold + (xFold - coord[0]), coord[1])
        elif fold[0] == 'y':
            yFold = int(fold[2:])
            if coord[1] > yFold:
                dotCoords[i] = (coord[0], yFold + (yFold - coord[1]))

dotCoords = list(dict.fromkeys(dotCoords))

xMax = 0
yMax = 0

for coord in dotCoords:
    if coord[0] > xMax:
        xMax = coord[0]
    if coord[1] > yMax:
        yMax = coord[1]

grid = [['.'] * (xMax + 1) for _ in range(yMax + 1)]

for coord in dotCoords:
    grid[coord[1]][coord[0]] = '#'

for line in grid:
    print(''.join(line))