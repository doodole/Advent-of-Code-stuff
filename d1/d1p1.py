with open('nums.txt') as nums:
    count = 0
    numbers = nums.readlines()
    for c, num in enumerate(numbers):
        if int(num) < int(numbers[c + 1]):
            count += 1
        if c + 1 == len(numbers) - 1:
            break
print(count)