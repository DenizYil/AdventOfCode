import math
from collections import defaultdict

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

ans = []

tracker = defaultdict(int)
ans = 0

for i, line in enumerate(lines):
    run = tracker.get(i, 0) + 1

    print("Running card", i + 1, ":", run)
    for r in range(run):

        s = line.split(":")
        winning, mine = s[1].split("|")

        winning = [int(x.strip()) for x in winning.split(" ") if x != ""]
        mine = [int(x.strip()) for x in mine.split(" ") if x != ""]

        wins = 0
        count = 0

        for m in mine:
            if m in winning:
                count += 1
                if wins == 0:
                    wins = 1
                else:
                    wins *= 2

        if count > 0:
            for j in range(i + 1 , i +1  + count):
                tracker[j] += 1
                ans += 1


print(ans)
print(ans + len(lines))
print(sum(tracker.values()) + len(lines))
