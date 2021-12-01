with open("./input.txt") as file:
    lines = file.readlines()

count = 0
last = int(lines[0])

for line in lines[1:]:
    num = int(line)
    
    if last < num:
        count += 1
    
    last = num

print(count)