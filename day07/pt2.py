with open("./input.txt") as file:
    nums = [int(line) for line in file.readline().split(",")]

brute = {}

for i in range(min(nums), max(nums)):
    brute[i] = 0
    for num in nums:
        diff = 0
        if num < i:
            diff = i - num
        elif num > i:
            diff = num - i

        add = 0

        for e in range(1, diff + 1):
            add += e

        brute[i] += add


print(min(brute.values()))