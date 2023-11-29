import string
import numpy as np

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    groups = [*np.array_split(lines, len(lines) / 3)]

ALHPABET = list(string.ascii_lowercase + string.ascii_uppercase)

count = 0
common = []

for group in groups:
    cm = []

    a, b, c = group

    for item in a:
        if item in b and item in c and item not in cm:
            cm.append(item)
    
    common.extend(cm)

count = sum([ALHPABET.index(c) + 1 for c in common])

# part 2
print(count)