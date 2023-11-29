with open("./input.txt") as file:
    lines = file.readlines()

hoz = 0
depth = 0
aim = 0

for line in lines:
    spl = line.split(" ")
    
    action = spl[0]
    amount = int(spl[1])

    if action == "forward":
        hoz += amount
        depth += aim * amount
        
    elif action == "down":
        aim += amount
    elif action == "up":
        aim -= amount


print(hoz * depth)