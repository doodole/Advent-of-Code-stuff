binaryNums = open('binary.txt', 'r')

binaryNums = list(map(lambda x: x[:-1], binaryNums.readlines()))

digitCount = {}

for num in binaryNums:
    for place, digit in enumerate(num[::-1]):
        if place in digitCount:
            digitCount[place][int(digit)] += 1
        else:
            if (int(digit) == 0):
                digitCount[place] = [1, 0]
            else:
                digitCount[place] = [0, 1]

gamma = 0
epsilon = 0

for i, counts in digitCount.items():
    if counts[1] > counts[0]:
        gamma += 2 ** i
    else:
        epsilon += 2 ** i

print(gamma, epsilon, gamma * epsilon)
