with open("./input.txt", "r") as file:
    lines = [l.strip() for l in file.read().split("\n")]


class Brick:
    def __init__(self, id) -> None:
        self.id = id
        self.location = (0, 0)
        self.previous = [self.location]
        self.last = None

    def move(self, new):
        self.location = new
        self.last = self.location

        if new not in self.previous:
            self.previous.append(new)


head = Brick("H")
tails = [Brick(index+1) for index in range(9)]

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

possible_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
possible_directions.extend(directions.values())


for line in lines:
    direction, amount = line.split()
    amount = int(amount)

    moveX, moveY = directions[direction]

    for i in range(amount):
        x, y = head.location
        head.move((x + moveX, y + moveY))

        for j in range(len(tails)):
            tail = tails[j]
            target = head if j == 0 else tails[j-1]

            selfX, selfY = tail.location
            targetX, targetY = target.location

            if max(abs(selfX - targetX), abs(selfY - targetY)) > 1:
                distanceX = targetX - selfX
                distanceY = targetY - selfY

                tail.move(
                    (
                        selfX + (distanceX / 2 if abs(distanceX)
                                 == 2 else distanceX),
                        selfY + (distanceY / 2 if abs(distanceY)
                                 == 2 else distanceY)
                    )
                )


print(tails[-1].previous)
print(len(tails[-1].previous))
