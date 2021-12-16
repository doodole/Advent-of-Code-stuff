tubeData = open('tubes.txt', 'r')

heights = list(map(lambda x: x[:-1],tubeData.readlines()))

total = 0

for row, heightRow in enumerate(heights):
    for col, height in enumerate(heightRow):
        height = int(height)
        directions = {
            'up': row - 1,
            'down': row + 1,
            'right': col + 1,
            'left': col - 1
        }
        for key, value in directions.items():
            if key in ['up', 'down'] and (value > len(heights) - 1 or value < 0):
                directions[key] = None
            if key in ['right', 'left'] and (value > len(heightRow) - 1 or value < 0):
                directions[key] = None
        min = True
        for key, value in directions.items():
            if value == None:
                continue
            if key in ['up', 'down']:
                if int(heights[value][col]) <= height:
                    min = False
                    break
            elif key in ['right', 'left']:
                if int(heights[row][value]) <= height:
                    min = False
                    break
        if min:
            total += height + 1

print(total)