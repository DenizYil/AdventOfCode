import math

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ans = []
gears = []

for row in range(len(lines)):
    for col in range(len(lines[row])):
        cell = lines[row][col]

        adjacents = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1)
        ]

        if cell.isdigit() or cell == ".":
            continue

        g = []

        for (r, c) in adjacents:
            adj_cell = lines[r][c]

            if adj_cell.isdigit():
                ans.append((r, c))

                if cell == "*":
                    g.append((r, c))

        gears.append(g)

checked = []

def get_number_from_cell(row, col):
    if (row, col) in checked:
        return 0

    cell = lines[row][col]
    assert cell.isdigit()

    numb = cell

    # check left
    for i in range(col - 1, -1, -1):
        if (row, i) in checked:
            break

        if not lines[row][i].isdigit():
            break
        else:
            checked.append((row, i))
            numb = lines[row][i] + numb

    # check right
    for i in range(col + 1, len(lines[row])):
        if (row, i) in checked:
            break

        if not lines[row][i].isdigit():
            break
        else:
            checked.append((row, i))
            numb += lines[row][i]

    return int(numb)

nums = []

for gear in gears:
    amount = []

    for (r, c) in gear:
        amount.append(get_number_from_cell(r, c))

    amount = list(x for x in amount if x != 0)

    if len(amount) == 2:
        nums.append(math.prod(amount))

print(nums)
print(sum(nums))