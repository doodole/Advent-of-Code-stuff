binaryNums = open('binary.txt', 'r')

binaryNums = list(map(lambda x: x[:-1], binaryNums.readlines()))

def getOxygenGeneratorRating(nums):
    digitCount = [0, 0]
    place = 0
    tempNums = []
    while len(nums) > 1:
        for num in nums:
            digitCount[int(num[place])] += 1
        if digitCount[0] > digitCount[1]:
            remove = "1"
        elif digitCount[0] < digitCount[1]:
            remove = "0"
        else:
            remove = "0"
        for num in nums:
            if num[place] != remove:
                tempNums.append(num)
        place += 1
        digitCount = [0, 0]
        nums = tempNums
        tempNums = []
    return int(nums[0], 2)

def getScrubberRating(nums):
    digitCount = [0, 0]
    place = 0
    tempNums = []
    while len(nums) > 1:
        for num in nums:
            digitCount[int(num[place])] += 1
        if digitCount[0] > digitCount[1]:
            remove = "0"
        elif digitCount[0] < digitCount[1]:
            remove = "1"
        else:
            remove = "1"
        for num in nums:
            if num[place] != remove:
                tempNums.append(num)
        place += 1
        digitCount = [0, 0]
        nums = tempNums
        tempNums = []
    return int(nums[0], 2)

o2Rating = getOxygenGeneratorRating(binaryNums)
scrubberRating = getScrubberRating(binaryNums)

print(o2Rating, scrubberRating, o2Rating * scrubberRating)






