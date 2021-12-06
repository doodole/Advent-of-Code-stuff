instructions = open('dive.txt', 'r')
instructionList = instructions.readlines()
def separateInstructions(i):
    return [i[:-3], i[-2]]

instructionList = map(separateInstructions, instructionList)
forward = 0
vertical = 0
aim = 0

for instruction, num in instructionList:
    num = int(num)
    if instruction == 'forward':
        forward += num
        vertical += aim * num
    elif instruction == 'up':
        aim -= num
    elif instruction == 'down':
        aim += num	
print(forward, vertical, forward * vertical)
