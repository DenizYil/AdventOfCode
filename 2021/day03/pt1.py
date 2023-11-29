with open("./input.txt") as file:
    lines = file.readlines()

l = []

for i in range(len(lines[0]) - 1):
    l.append([])

for line in lines:
    for i in range(len(line.strip())):
        l[i].append(line[i])

gamma = ""
epsilon = ""

for column in l:
    zeros, ones = 0, 0

    for numb in column:
        if numb == "0":
            zeros += 1
        else:
            ones += 1

    gamma += "1" if zeros < ones else "0"
    epsilon += "0" if zeros < ones else "1"

print(gamma)
print(int(gamma, 2))

print(epsilon)
print(int(epsilon, 2))

print("Multiplied:", (int(gamma, 2) * int(epsilon, 2)))