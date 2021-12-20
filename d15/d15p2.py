caveData = open('cave.txt', 'r')

caveData = list(map(lambda x: list(x[:-1]), caveData.readlines()))

def getRiskFromStart(x):
    return x.riskFromStart

filterPoint = None

def filterForPoint(x):
    if x.point != filterPoint:
        return True
    return False

q = []

class Node:
    point = None

    def __init__(self, point, risk, riskFromStart = 54363446346223643225645, discovered = False, parent = None):
        self.point = point
        self.risk = risk
        self.riskFromStart = riskFromStart
        self.discovered = discovered
        self.parent = parent

    def getNeighbors(self):
        directions = [(self.point[0] - 1, self.point[1]), (self.point[0] + 1, self.point[1]), (self.point[0], self.point[1] + 1),(self.point[0], self.point[1] - 1)]
        newDirections = []
        for value in directions:
            if (self.parent != None and value == self.parent.point) or (value[0] > len(cave) - 1 or value[0] < 0) or (value[1] > len(cave[0]) - 1 or value[1] < 0) or (cave[value[0]][value[1]].discovered):
                continue
            newDirections.append(value)
        return newDirections

    def getRisk(self):
        return self.risk


cave = []

for row, points in enumerate(caveData):
    tempRow = []
    for col, risk in enumerate(points):
        tempRow.append(Node((row , col), int(risk)))

    tempTempRow = []

    for i in range(1, 5):
        for col, node in enumerate(tempRow):
            r = node.getRisk() + i
            if r > 9:
                r -= 9
            tempTempRow.append(Node((row, col + len(caveData[0]) * i), r))
    
    tempRow.extend(tempTempRow)

    cave.append(tempRow)
    
chunk = []
for i in range (1, 5):
    for row, nodes in enumerate(cave):
        tempRow = []
        for col, node in enumerate(nodes):
            r = node.getRisk() + i
            if r > 9:
                r -= 9
            tempRow.append(Node((row + len(caveData) * i, col), r))
        chunk.append(tempRow)
        
for row in chunk:
    cave.append(row)


cave[0][0].riskFromStart = 0

start = cave[0][0]

q.append(start)

while q:
    currentNode = q.pop()
    currentNode.discovered = True

    if cave[len(cave) - 1][len(cave[0]) - 1].discovered:
        break

    for neighbor in currentNode.getNeighbors():
        neighborNode = cave[neighbor[0]][neighbor[1]]

        minRisk = min(neighborNode.riskFromStart, currentNode.riskFromStart + neighborNode.risk)

        if minRisk != neighborNode.riskFromStart:
            neighborNode.riskFromStart = minRisk
            neighborNode.parent = currentNode
            
        filterPoint = neighborNode.point
            
        q = list(filter(filterForPoint, q))
        q.append(neighborNode)

    q.sort(key=getRiskFromStart, reverse=True)

print(cave[len(cave) - 1][len(cave[0]) - 1].point, cave[len(cave) - 1][len(cave[0]) - 1].riskFromStart)
