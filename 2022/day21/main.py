with open("./input.txt", "r") as file:
    lines = [l for l in file.read().split("\n")]

monkeys = {}

for monkey in lines:
    name, rest = monkey.split(": ")

    try:
        i = int(rest)
        monkeys[name] = i
        continue
    except ValueError:
        pass

    monkeys[name] = rest.split()


root = monkeys["root"]

def e(name):
    value = monkeys[name]

    if isinstance(value, int):
        return value

    left = e(value[0])
    right = e(value[2])

    return eval(f"{left} {value[1]} {right}")

print(e("root"))