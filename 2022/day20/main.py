class Node:
    def __init__(self, id, item):
            self.id = id
            self.value = item
            self.prev = None
            self.next = None

    def __str__(self):
        return f"{self.value}"

    def __repr__(self) -> str:
        return str(self)


with open("./input.txt", "r") as file:
    lines = [l.strip() for l in file.read().split("\n")]


items = []

for i, line in enumerate(lines):
    items.append(Node(i, int(line)))


def get(_id):
    for i, item in enumerate(items):
        if item.id == _id:
            return (i, item)


for i in range(len(lines)):
    print(items)

    index, item = get(i)
    print("GET:", get(i))

    if item.value > 0:
        for j in range(1, item.value+1):
            index = index + j
            print("Index", index)

            if index == len(items):
                index = 0

            items.remove(item)
            items.insert(index, item)

    elif item.value < 0:
        for j in range(1, abs(item.value)+1):
            index = index + j

            if index == 0:
                index = len(items)-1

            items.remove(item)
            items.insert(index, item)
