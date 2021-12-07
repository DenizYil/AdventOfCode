with open("./input.txt") as file:
    input = [int(line) for line in file.readline().split(",")]

fishs = {}

for i in range(9):
    fishs[i] = input.count(i)

for day in range(256):
    new = {}

    new[0] = fishs[1]
    new[1] = fishs[2]
    new[2] = fishs[3]
    new[3] = fishs[4]
    new[4] = fishs[5]
    new[5] = fishs[6]
    new[6] = fishs[7] + fishs[0]
    new[7] = fishs[8]
    new[8] = fishs[0]

    fishs = new

print(new)
print(sum(new.values()))