clockData = open('clock.txt', 'r')

clocks = list(map(lambda x: x[:-1].split(' | '), clockData.readlines()))

for i, clock in enumerate(clocks):
    clocks[i] = list(map(lambda x: x.split(' '), clock))
    clocks[i][0].sort(key=len)

def testDigit(testDigit, knownDigit):
    for char in knownDigit:
        testDigit = testDigit.replace(char, '')
    return len(testDigit)

total = 0

for i, clock in enumerate(clocks):
    digits = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    }
    for digit in clocks[i][0]:
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            digits[1] = digit
        elif len(digit) == 3:
            digits[7] = digit
        elif len(digit) == 4:
            digits[4] = digit
        elif len(digit) == 5:
            if testDigit(digit, digits[1]) == 3:
                digits[3] = digit
                continue
            if testDigit(digit, digits[4]) == 2:
                digits[5] = digit
                continue
            digits[2] = digit
        elif len(digit) == 6:
            if testDigit(digit, digits[4]) == 2:
                digits[9] = digit
                continue
            if testDigit(digit, digits[1]) == 4:
                digits[0] = digit
                continue
            digits[6] = digit
        elif len(digit) == 7:
            digits[8] = digit

    tot = 0
    for digit in clocks[i][1]:
        keys = list(digits.keys())
        values = list(digits.values())
        tot = tot * 10 + keys[values.index(''.join(sorted(digit)))]
    total += tot

print(total)
