with open("./input.txt") as file:
    fishs = [int(line) for line in file.readline().split(",")]

for day in range(80):
    add = 0
    for i in range(len(fishs)):
        fishs[i] = fishs[i] - 1

        if fishs[i] == -1:
            fishs[i] = 6
            add += 1

    if add != 0:
        for i in range(add):
            fishs.append(8)

    
print(len(fishs))