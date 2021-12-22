targetAreaX = [60, 94]
targetAreaY = [-171, -136]

maxXVel = max(targetAreaX)
minXVel = 0

maxX = 0

while abs(maxX) < min(list(map(lambda x: abs(x), targetAreaX))):
    maxX = 0
    if max(targetAreaX) < 0:
        min -= 1
    else:
        minXVel += 1
    if minXVel > 0:
        for i in range(1, minXVel + 1):
            maxX += i
    elif minXVel < 0:
        for i in range(1, minXVel * -1 + 1):
            maxX -= i

maxYVel = abs(min(targetAreaY))
minYVel = min(targetAreaY)

potentialTrajectories = []

for x in range (minXVel, maxXVel + 1):
    for y in range(minYVel, maxYVel + 1):
        potentialTrajectories.append((x, y))

total = 0

for trajectory in potentialTrajectories:
    xVel = trajectory[0]
    yVel = trajectory[1]
    x = 0
    y = 0
    inTargetArea = False
    while not inTargetArea:
        x += xVel
        y += yVel

        yVel -= 1

        if xVel > 0:
            xVel -= 1
        elif xVel < 0:
            xVel += 1
        if min(targetAreaX) <= x <= max(targetAreaX) and  min(targetAreaY) <= y <= max(targetAreaY):
            inTargetArea = True
        
        if x > max(targetAreaX) or y < min(targetAreaY):
            break
    if inTargetArea:
        total += 1

print(total)