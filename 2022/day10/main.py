with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.read().split("\n")]

cycle = 0
x = 1

saved = []

for line in lines:
    if line == "noop":
        cycle += 1

    if line != "noop":
        _, amount = line.split()
        amount = int(amount)

        cycle += 1

        if cycle in (20, 60, 100, 140, 180, 220):
            print((cycle, x))
            saved.append(cycle * x)
        if cycle == 220:
            break

        x += amount
        cycle += 1

    if cycle in (20, 60, 100, 140, 180, 220):
        saved.append(cycle * x)

print(sum(saved))