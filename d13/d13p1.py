dotsData = open('dots.txt', 'r')

dotsData = list(map(lambda x: x[:-1], dotsData.readlines()))

linebreak = dotsData.index('')

dotCoords = list(map(lambda x: tuple(map(int, x.split(','))), dotsData[:linebreak]))

folds = list(map(lambda x: x.split(' ')[-1], dotsData[linebreak + 1:]))

xFold = 655

for i, coord in enumerate(dotCoords):
    if coord[0] > xFold:
        dotCoords[i] = (xFold + (xFold - coord[0]), coord[1])

print(len(list(dict.fromkeys(dotCoords))))
