clockData = open('clock.txt', 'r')

clocks = list(map(lambda x: x[:-1].split(' | '), clockData.readlines()))

for i, clock in enumerate(clocks):
    clocks[i] = tuple(map(lambda x: x.split(' '), clock))

total = 0

for i, clock in enumerate(clocks):   
    for digit in clocks[i][1]:
        if len(digit) in set((7, 4, 3 , 2)):
            total += 1

print(total)
