with open("./input.txt") as file:
    lines = file.readlines()

hoz = 0
depth = 0

for line in lines:
    spl = line.split(" ")
    
    action = spl[0]
    amount = int(spl[1])

    if action == "forward":
        hoz += amount
    elif action == "down":
        depth += amount
    elif action == "up":
        depth -= amount

print(hoz * depth)