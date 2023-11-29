with open("./input.txt", "r") as file:
    lines = file.readlines()

count = 0
last = int(lines[0])

for line in lines[1:]:
    if last < int(line):
        count += 1
    last = int(line)

print(count)