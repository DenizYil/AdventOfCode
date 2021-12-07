import copy

with open("./input.txt") as file:
    lines = [line for line in file.readlines()]

l = []

for line in lines:
    l.append(line.strip())

def count(l, i):
    zeros, ones = 0, 0
    for element in l:
        if element[i] == "0":
            zeros += 1
        else:
            ones += 1

    return zeros, ones

def filter(l, i, up: bool):
    if len(l) == 1:
        return l
    
    zeros, ones = count(l, i)

    key = ("1" if up else "0") if zeros < ones or zeros == ones else ("0" if up else "1")

    for element in copy.copy(l):
        if element[i] != key:
            l.remove(element)
            
        if len(l) == 1:
            return l
    
    return filter(l, i+1, up)

oxr = filter(copy.copy(l), 0, True)[0]
csr = filter(copy.copy(l), 0, False)[0]

print(int(oxr, 2) * int(csr, 2))
