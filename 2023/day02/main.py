import math
from collections import defaultdict

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

p1, p2 = [], []

for line in lines:
    _id = int(line.split(":")[0].split(" ")[1])
    items = list(item.strip() for item in line.split(":")[1].strip().split(";"))

    invalid = False
    tracker = defaultdict(list)

    for cube in items:
        for x in cube.split(", "):
            num, color = x.split(" ")
            num = int(num)

            tracker[color].append(num)

            if color == "red" and num > 12:
                invalid = True

            if color == "green" and num > 13:
                invalid = True

            if color == "blue" and num > 14:
                invalid = True

    if not invalid:
        p1.append(_id)

    p2.append(math.prod(max(v) for v in tracker.values()))

print(sum(p1))
print(sum(p2))





