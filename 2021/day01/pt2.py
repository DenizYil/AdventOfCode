with open("./input.txt") as file:
    lines = file.readlines()

numbs = []

index = 0
while index != len(lines) - 2:
    l = []

    for i in range(3):
        l.append(int(lines[index + i]))
    
    index += 1
    numbs.append(l)

count = 0
last = sum(numbs[0])

for num in numbs[1:]:
    if last < sum(num):
        count += 1
    last = sum(num)

print(count)