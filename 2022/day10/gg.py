with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.read().split("\n")]

cycle = 0
x = 1

saved = []
SAVING_CYCLES = (20, 60, 100, 140, 180, 220)

grid = [["-" for _ in range(40)] for _ in range(6)]

row = 0
column = 0

def inc():
    global cycle, x, row, column

    grid[row][column] = "#" if abs(x-column) <= 1 else "."

    if column == 39:
        row += 1
        column = 0
    else:
        column += 1

    cycle += 1


    if cycle in SAVING_CYCLES:
        saved.append(cycle * x)

for line in lines:
    if line == "noop":
        inc()
        continue

    if line != "noop":
        _, amount = line.split()
        amount = int(amount)

        inc()
        inc()

        x += amount
        continue

print(sum(saved))

for x in grid:
    print("".join(x))