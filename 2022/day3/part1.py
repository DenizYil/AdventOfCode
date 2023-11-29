import string

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ALPHABET = list(string.ascii_lowercase + string.ascii_uppercase)

count = 0
common = []

for line in lines:
    length = int(len(line) / 2)

    a, b = line[:length], line[length:]
    
    cm = []

    for item in a:
        if item in b and item not in cm:
            cm.append(item)

    common.extend(cm)

count = sum([ALPHABET.index(c) + 1 for c in common])

# part 1
print(count)