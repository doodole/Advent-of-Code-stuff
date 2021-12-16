tubeData = open('tubes.txt', 'r')

heights = list(map(lambda x: x[:-1],tubeData.readlines()))

basins = {}

points = {}

def searchForPoints(point, height):
    if height == 9:
        return
    directions = points[point]
    inBasin = False
    for basin in basins:
        if point in basins[basin]['points']:
            inBasin = True
        else: 
            continue
        for adjPoint in directions.values():
            if adjPoint == None:
                continue
            elif adjPoint not in basins[basin]['points'] and int(heights[adjPoint[0]][adjPoint[1]]) != 9:
                basins[basin]['points'].append(adjPoint)
                basins[basin]['size'] += 1
                searchForPoints(adjPoint, int(heights[adjPoint[0]][adjPoint[1]]))
    if not inBasin:
        basinIds = list(basins.keys())
        if len(basinIds) == 0:
            basins[0] = {
                'points': [point],
                'size': 1
            }
        else:
            basins[basinIds[-1] + 1] = {
                'points': [point],
                'size': 1
            }
        searchForPoints(point, height)

for row, heightRow in enumerate(heights):
    for col, height in enumerate(heightRow):
        height = int(height)
        directions = {
            'up': (row - 1, col),
            'down': (row + 1, col),
            'right': (row, col + 1),
            'left': (row, col - 1),
        }
        for key, value in directions.items():
            if key in ['up', 'down'] and (value[0] > len(heights) - 1 or value[0] < 0):
                directions[key] = None
            if key in ['right', 'left'] and (value[1] > len(heightRow) - 1 or value[1] < 0):
                directions[key] = None
        
        points[(row, col)] = directions

for row, heightRow in enumerate(heights):
    for col, height in enumerate(heightRow):
        searchForPoints((row, col), int(height))

sizes = []

for basin in basins:
    sizes.append(basins[basin]['size'])

sizes.sort(reverse=True)

multiplied = 1

for val in sizes[:3]:
    multiplied *= val

print(multiplied)
