with open("./input.txt") as file:
    nums = [int(line) for line in file.readline().split(",")]

brute = {}

for i in range(min(nums), max(nums)):
    brute[i] = 0
    for num in nums:
        if num < i:
            brute[i] = brute[i] + (i - num)
        elif num > i:
            brute[i] = brute[i] + (num - i)

print(min(brute.values()))