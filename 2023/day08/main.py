with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    instructions = lines[0]
    m = {}

    for line in lines[2:]:
        parts = line.split(" = ")
        m[parts[0]] = eval(parts[1].replace("(", '("').replace(", ", '", "').replace(")", '")'))


curr = "AAA"
i = 0
while curr != "ZZZ":
    for instruction in list(instructions):
        (left, right) = m[curr]
        if instruction == "R":
            curr = right
        else:
            curr = left

        i += 1

print(i)