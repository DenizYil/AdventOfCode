import math
from collections import deque

def calc(w, operation):
    first, op, second = operation
    x, y = 0, 0

    if first == "old":
        x = w
    else:
        x = int(first)

    if second == "old":
        y = w
    else:
        y = int(second)

    if op == "+":
        return x + y
    else:
        return x * y


class Monkey:

    def __init__(self, _id, items, operation, test, success, failure) -> None:
        self._id = _id
        self.items = deque(items)
        self.operation = operation
        self.test = test
        self.success = success
        self.failure = failure
        self.count = 0


monkeys = []

with open("./input.txt", "r") as file:

    for m in file.read().split("\n\n"):
        lines = [l.strip() for l in m.split("\n")]

        _id = int(lines[0][7:-1])
        items = list(int(x) for x in lines[1].replace("Starting items: ", "").split(", "))
        operation = lines[2].replace("Operation: ", "").replace("new = ", "").strip().split()
        test = int(lines[3].split()[-1])
        success = int(lines[4].split()[-1])
        failure = int(lines[5].split()[-1])

        monkeys.append(Monkey(_id, items, operation, test, success, failure))

lcm = math.lcm(*list(monkey.test for monkey in monkeys))

for round in range(10000):
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            worry = monkey.items.pop()
            worry = calc(worry, monkey.operation)
            worry %= lcm


            monkey.count += 1

            if worry % monkey.test == 0:
                m = monkeys[monkey.success]
            else:
                m = monkeys[monkey.failure]

            m.items.append(worry)

    if round % 1000 == 0 or round == 20:
        print(round)
        print(sorted(monkey.count for monkey in monkeys))

for monkey in monkeys:
    print(monkey.items)

print(sorted(monkey.count for monkey in monkeys))
