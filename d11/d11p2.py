octopusData = open('octopus.txt', 'r')

octopus = list(map(lambda x: list(x[:-1]), octopusData.readlines()))

def flash(o, row, col):
    if o == 10:
        octopus[row][col] += 1
        directions = {
            'up': (row - 1, col),
            'down': (row + 1, col),
            'right': (row, col + 1),
            'left': (row, col - 1),
            'upright': (row - 1, col + 1),
            'upleft': (row - 1, col - 1),
            'downright': (row + 1, col + 1),
            'downleft': (row + 1, col - 1),
        }

        for key, value in directions.items():
            if key in ['up', 'down'] and (value[0] > len(octopus) - 1 or value[0] < 0):
                directions[key] = None
                directions[key + 'left'] = None
                directions[key + 'right'] = None
            if key in ['right', 'left'] and (value[1] > len(octopus[0]) - 1 or value[1] < 0):
                directions[key] = None
                directions['up' + key] = None
                directions['down' + key] = None
        
        for key, coord in directions.items():
            if coord == None:
                continue
            if octopus[coord[0]][coord[1]] < 10:
                octopus[coord[0]][coord[1]] += 1
                flash(octopus[coord[0]][coord[1]], coord[0], coord[1])
        
steps = 0
allFlash = False

while not allFlash:
    for row, octoLine in enumerate(octopus):
        for col, o in enumerate(octoLine):
            octopus[row][col] = int(o) + 1

    for row, octoLine in enumerate(octopus):
        for col, o in enumerate(octoLine):
            flash(o, row, col)

    countFlash = 0
    for row, octoLine in enumerate(octopus):
        for col, o in enumerate(octoLine):
            if o == 11:
                octopus[row][col] = 0
                countFlash += 1
    
    if countFlash == 100:
        allFlash = True
    
    steps += 1



print(steps)