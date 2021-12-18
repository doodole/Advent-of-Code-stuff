pathData = open('paths.txt', 'r')

paths = list(map(lambda x: list(x[:-1].split('-')), pathData.readlines()))

routes = []

def pathFind(cave, route=[]):
    newRoute = route.copy()

    newRoute.append(cave)
    
    if 'end' in newRoute:
        routes.append(newRoute)
        return

    for path in paths:
        if cave in path:
            i = path.index(cave)
            if i == 0:
                nextCave = path[1]
            else:
                nextCave = path[0]
            
            if (nextCave == 'start' or nextCave == 'end') and nextCave in newRoute:
                continue
            
            if nextCave.islower() and nextCave in newRoute:
                skip = False
                smallCaves = list(filter(lambda x: x.islower(), newRoute))
                for c in smallCaves:
                    caveCount = smallCaves.count(c)
                    if caveCount > 1:
                        skip = True
                        break
                if skip:
                    continue

            pathFind(nextCave, newRoute)

pathFind('start')

print(len(routes))