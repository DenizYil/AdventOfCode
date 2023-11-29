with open("./input.txt", "r") as file:
    lines = [l.strip() for l in file.read().split("\n")]

class Brick:
    def __init__(self) -> None:
        self.location = (0, 0)
        self.previous = [self.location]
        self.last = None

    def move(self, new):
        self.last = self.location
        self.location = new

        if new not in self.previous:
            self.previous.append(new)

head = Brick()
tail = Brick()

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

possible_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
possible_directions.extend(directions.values())

def is_close():
    if head.location == tail.location:
        return True

    near = False

    tailX, tailY = tail.location

    for direction in possible_directions:
        x, y = direction

        if (x + tailX, y + tailY) == head.location:
            near = True

    return near

for line in lines:
    direction, amount = line.split()
    amount = int(amount)

    moveX, moveY = directions[direction]

    for i in range(amount):
        x, y = head.location
        head.move((x + moveX, y + moveY))

        if not is_close():
            tail.move(head.last)


print(tail.previous)
print(len(tail.previous))
