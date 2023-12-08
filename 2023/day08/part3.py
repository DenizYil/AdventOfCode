import math
from collections import defaultdict

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    instructions = lines[0]
    m = {}

    for line in lines[2:]:
        parts = line.split(" = ")
        m[parts[0]] = eval(parts[1].replace("(", '("').replace(", ", '", "').replace(")", '")'))

nodes = [k for k in m.keys() if k.endswith("A")]
dupes = [False] * len(nodes)
tracker = defaultdict(list)

count = 0
s = ""

found = [0] * len(nodes)
counter = [0] * len(nodes)

for j, curr in enumerate(nodes):
    if curr in tracker[j]:
        dupes[j] = True

    tracker[j].append(curr)

    while not curr.endswith("Z"):
        for instruction in list(instructions):
            (left, right) = m[curr]

            if instruction == "R":
                curr = right
            else:
                curr = left

            counter[j] += 1

            if curr.endswith("Z") and found[j] == 0:
                found[j] = counter[j]

            if all(x != 0 for x in found):
                print(found)
                print(" ".join(str(x) for x in found))
                print(math.lcm(*found))
                exit()

    nodes[j] = curr
    count += 1


print(tracker)
print(list(len(x) for x in tracker.values()))
