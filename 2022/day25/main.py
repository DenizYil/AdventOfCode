import math

with open("./input.txt") as file:
    lines = [l.strip() for l in file.read().split("\n")]


def value(item):
    if item == "-":
        return -1
    elif item == "=":
        return -2
    else:
        return int(item)

summed = 0

for line in lines:
    length = len(line) - 1

    for char in line:
        summed += value(char) * math.pow(5, length)
        length -= 1


print(summed)


