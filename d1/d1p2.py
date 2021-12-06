with open('nums.txt') as nums:
    count = 0
    numbers = nums.readlines()
    for c, num in enumerate(numbers):
        a = int(num) + int(numbers[c + 1]) + int(numbers[c + 2])
        b = int(numbers[c + 1]) + int(numbers[c + 2]) + int(numbers[c + 3])
        if a < b:
            count += 1
        if c + 4 > len(numbers) - 1:
            break
print(count)