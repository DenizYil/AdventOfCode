import math

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

possible_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
possible_directions.extend(directions.values())

targetX, targetY = (4, 4)
tailX, tailY = (3, 2)

# we need to find the smallest direction
minimum_dist, minimum_dir = 0, ()
for direction in possible_directions:
    x, y = direction


    dist = math.sqrt(
        math.pow(abs(x + tailX) - targetX, 2) + math.pow(abs(y + tailY) - targetY, 2)
    )

    if dist > minimum_dist:
        minimum_dist = dist
        minimum_dir = direction

print(minimum_dir)