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

def getPacketValue(p):
    originalLen = len(p)
    if getType(p) == 4:
        p = deencapsulate(p, 6)
        tempBin = ""

        while int(p[0]) != 0:
            tempBin += p[1:5]
            p = deencapsulate(p, 5)

        tempBin += p[1:5]

        p = deencapsulate(p, 5)

        return (int(tempBin, 2), originalLen - len(p))
    elif getType(p) == 0:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            total = 0
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                total += res[0]

                p = deencapsulate(p, res[1])

            return (total, originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            total = 0
            for _ in range(num):
                res = getPacketValue(p)

                total += res[0]

                p = deencapsulate(p, res[1])

            return (total, originalLen - len(p))

    elif getType(p) == 1:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            product = 1
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                product *= res[0]

                p = deencapsulate(p, res[1])

            return (product, originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            product = 1
            for _ in range(num):
                res = getPacketValue(p)

                product *= res[0]

                p = deencapsulate(p, res[1])

            return (product, originalLen - len(p))

    elif getType(p) == 2:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            nums = []
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (min(nums), originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            nums = []
            for _ in range(num):
                res = getPacketValue(p)

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (min(nums), originalLen - len(p))

    elif getType(p) == 3:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            nums = []
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (max(nums), originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            nums = []
            for _ in range(num):
                res = getPacketValue(p)

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (max(nums), originalLen - len(p))

    elif getType(p) == 5:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            nums = []
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (int(nums[0] > nums[1]), originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            nums = []
            for _ in range(num):
                res = getPacketValue(p)

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (int(nums[0] > nums[1]), originalLen - len(p))

    elif getType(p) == 6:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            nums = []
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                nums.append(res[0])

                p = deencapsulate(p, res[1])
                
            return (int(nums[0] < nums[1]), originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            nums = []
            for _ in range(num):
                res = getPacketValue(p)

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (int(nums[0] < nums[1]), originalLen - len(p))

    elif getType(p) == 7:
        if getLenId(p) == 0:
            bits = getSubpacketBits(p)
            bitsSearched = 0

            p = deencapsulate(p, 22)

            nums = []
            while bitsSearched < bits:
                res = getPacketValue(p)

                bitsSearched += res[1]

                nums.append(res[0])

                p = deencapsulate(p, res[1])
                
            return (int(nums[0] == nums[1]), originalLen - len(p))

        if getLenId(p) == 1:
            num = getSubpacketNum(p)

            p = deencapsulate(p, 18)

            nums = []
            for _ in range(num):
                res = getPacketValue(p)

                nums.append(res[0])

                p = deencapsulate(p, res[1])

            return (int(nums[0] == nums[1]), originalLen - len(p))

print(getPacketValue(binary))