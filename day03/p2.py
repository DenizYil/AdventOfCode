import copy

with open("./input.txt") as file:
    lines = [line for line in file.readlines()]

l = []

for i in range(len(lines[0]) - 1):
    l.append([])

for line in lines:
    for i in range(len(line.strip())):
        l[i].append(line[i])

gamma = ""  
epsilon = ""


remove = copy.copy([line.strip() for line in lines])
index = 0

for column in l:
    zeros, ones = 0, 0

    for numb in column:
        if numb == "0":
            zeros += 1
        else:
            ones += 1

    key = "1" if zeros < ones or zeros == ones else "0"

    for re in copy.copy(remove):
        if re[index] != key:
            remove.remove(re)


    index += 1

    gamma += "1" if zeros < ones else "0"
    epsilon += "0" if zeros < ones else "1"

print(remove)

print(gamma)
print(int(gamma, 2))

print(epsilon)
print(int(epsilon, 2))

print("Multiplied:", (int(gamma, 2) * int(epsilon, 2)))
