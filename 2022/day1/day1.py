with open("./input.txt", "r") as f:
    numbers = [sum([int(x) for x in l.split("\n")])for l in f.read().split("\n\n")]


# 1
print(max(numbers))

#2
numbers.sort()
print(numbers[-1] + numbers[-2] + numbers[-3])

