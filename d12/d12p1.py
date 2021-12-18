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
            
            if nextCave.islower() and nextCave in newRoute:
                continue
            
            pathFind(nextCave, newRoute)

pathFind('start')

print(len(routes))
