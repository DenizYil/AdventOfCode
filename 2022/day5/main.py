with open("./input.txt", "r") as file:
    crates, commands = file.read().split("\n\n")

    crates = crates.split("\n")
    commands = commands.split("\n")

    indexes = crates.pop()
    indexes = list(filter(lambda i: i != 0, [indexes.index(i) for i in indexes]))

    actual_crates = [[] for _ in range(len(indexes))]
    
    for i in range(len(crates)):
        crate = crates[i]
        count = 0
        for j in range(len(crate)):
            char = crate[j]

            if not char.isalpha():
                continue

            actual_crates[indexes.index(crate.index(char))].append(char)

            if crate.count(char) != 1:
                crate = crate.replace(char, ' ', 1)

    for i in range(len(actual_crates)):
        actual_crates[i] = list(reversed(actual_crates[i]))


def part_one():
    for command in commands:
        
        _, amount, _, from_crate, _, to_crate = [s.strip() for s in command.split(" ")]

        amount = int(amount)
        from_crate = int(from_crate) - 1
        to_crate = int(to_crate) - 1

        for _ in range(int(amount)):
            removed = actual_crates[from_crate].pop()
            actual_crates[to_crate].append(removed)
            
    s = "".join(crate[-1] for crate in actual_crates)
    print("Part 1", s)

def part_two():
    for command in commands:
        _, amount, _, from_crate, _, to_crate = [s.strip() for s in command.split(" ")]

        amount = int(amount)
        from_crate = int(from_crate) - 1
        to_crate = int(to_crate) - 1


        to_add = []

        for _ in range(int(amount)):
            removed = actual_crates[from_crate].pop()
            to_add.append(removed)

        
        actual_crates[to_crate].extend(reversed(to_add))

            
    s = "".join(crate[-1] for crate in actual_crates)
    print("Part 2", s)

part_one()
part_two()
