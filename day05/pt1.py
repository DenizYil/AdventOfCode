with open("./input.txt") as file:
    lines = [line for line in file.readlines()]

input = []

for line in lines:
    l = line.split("->")

    pair = []
    
    pair.append((int(l[0].split(",")[0]), int(l[0].split(",")[1])))
    pair.append((int(l[1].split(",")[0]), int(l[1].split(",")[1])))

    input.append(pair)

grid = [[]]

print(input)

print(grid)