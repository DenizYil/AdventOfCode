with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

p1 = []

for line in lines:
    s = line.split(":")
    winning, mine = s[1].split("|")

    winning = [int(x.strip()) for x in winning.split(" ") if x != ""]
    mine = [int(x.strip()) for x in mine.split(" ") if x != ""]

    wins = 0

    for m in mine:
        if m in winning:
            if wins == 0:
                wins = 1
            else:
                wins *= 2

    p1.append(wins)

print(sum(p1))

