hexNum = open('hex.txt', 'r').readline()

binary = bin(int(hexNum, 16))[2:].zfill(len(hexNum) * 4)

def getVersion(b):
    return int(b[0:3], 2)

def getType(b):
    return int(b[3:6], 2)

def getLenId(b):
    return int(b[6])

def getSubpacketBits(b):
    return int(b[7:22], 2)

def getSubpacketNum(b):
    return int(b[7:18], 2)

def deencapsulate(b, i):
    return b[i:]    

total = 0
while len(binary) != 0:
    total += getVersion(binary)

    if getType(binary) != 4:
        if getLenId(binary) == 0:
            binary = deencapsulate(binary, 22)
        else:
            binary = deencapsulate(binary, 18)
    else:
        binary = deencapsulate(binary, 6)

        while(int(binary[0]) != 0):
            binary = deencapsulate(binary, 5)
        binary = deencapsulate(binary, 5)
    
    if not list(filter(lambda x: int(x) != 0, binary)):
        break



print(total)