with open("./input.txt", "r") as file:
    lines = [l.strip() for l in file.read().split("\n")]

class Brick:
    def __init__(self, id) -> None:
        self.id = id
        self.location = (0, 0)
        self.previous = [self.location]
        self.last = None

    def move(self, new):
        self.last = self.location
        self.location = new

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



def handle():
    for i in range(len(tails)):
        tail = tails[i]
        target = head if i == 0 else tails[i-1]

        # print("Index:", i)
        # print("Target:", target.location, "----", target.id)
        # print("Self:", tail.location, "----", tail.id)

        if target.location == tail.location:
            # print()
            continue

        near = False

        tailX, tailY = tail.location

        for direction in possible_directions:
            x, y = direction

            if (x + tailX, y + tailY) == target.location:
                near = True


        # print("Near?", near)


        if not near:
            # print("Moving...")
            # print(target.__dict__)
            tail.move(target.last)
            # print("New location:", tail.location)

        # print()


for line in lines:
    direction, amount = line.split()
    amount = int(amount)

    moveX, moveY = directions[direction]

    print("COMMAND:", line)

    for i in range(amount):
        x, y = head.location
        head.move((x + moveX, y + moveY))
        print("HEAD LOCATION:", head.location)
        print("HEAD LAST", head.last)

        handle()



print(tails[-1].previous)
print(len(tails[-1].previous))


