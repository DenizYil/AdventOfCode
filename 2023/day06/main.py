import math

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    times = [int(x) for x in lines[0].split(": ")[1].split(" ") if x]
    distances = [int(x) for x in lines[1].split(": ")[1].split(" ") if x]

ans = []
for part in range(2):
    if part == 1:
        times = [int("".join(str(x) for x in times))]
        distances = [int("".join(str(x) for x in distances))]

    for i, time in enumerate(times):
        total_distances = []

        for speed in range(time):
            total_distance = speed * abs(time - speed)
            if total_distance > distances[i]:
                total_distances.append(total_distance)

        ans.append(len(total_distances))

    if part == 0:
        print("p1", math.prod(ans))
    else:
        print("p2", ans[-1])





