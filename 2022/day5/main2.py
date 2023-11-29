with open("./input.txt", "r") as file:
    crates, commands = file.read().split("\n\n")

    crates = crates.split("\n")
    commands = commands.split("\n")

    actual_crates = [[] for _ in range(9)]

    for i in range(1, 35, 4):
        for j in range(len(crates)):
            item = crates[j][i]

            if item.isalpha():
                actual_crates[int(crates[-1][i])-1].append(item)

    for i in range(len(actual_crates)):
        actual_crates[i] = list(reversed(actual_crates[i]))
    
    


def part_one(actual_crates):
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

def part_two(actual_crates):
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

part_one(list(actual_crates.copy()))
part_two(list(actual_crates))
