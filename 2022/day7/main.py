with open("./input.txt") as file:
    lines = [line for line in file.read().split("\n")]
    lines.pop(0)


class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.files: list[int] = []
        self.directories = {}

    def print(self, depth=0) -> str:
        final = f"{' ' * depth}- {self.name} (dir) (sum: {self.size()}): \n"

        for directory in self.directories.values():
            final += directory.print(depth + 2) + "\n"

        for file in self.files:
            final += f"{' ' * (depth + 2)}- {str(file)} (file) \n"

        return final

    def size(self) -> int:
        size = sum([directory.size()
                   for directory in self.directories.values()])
        size += sum(self.files)
        return size

    def __str__(self) -> str:
        return self.print(0)


main = Directory("/", None)
current = main

for command in lines:
    parts = command.split()

    # It's a regular file
    try:
        current.files.append(int(parts[0]))
    except ValueError:
        pass

    # Make a directory
    if parts[0] == "dir":
        current.directories[parts[1]] = Directory(parts[1], current)

    elif command.startswith("$ cd"):
        current = current.parent if parts[-1] == '..' else current.directories[parts[-1]]


def get_sizes(current):
    sizes = []

    for directory in current.directories.values():
        sizes.extend(get_sizes(directory))

    sizes.append(current.size())
    return sizes


sizes = sorted(get_sizes(main))

print("Part A", sum(filter(lambda x: x <= 100000, sizes)))
print("Part B", next(filter(lambda exclude: 70000000 - (sizes[-1]-exclude) >= 30000000, sizes)))