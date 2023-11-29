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

    if name == "root":
        return eval(f"{left} == {right}")



    return eval(f"{left} {value[1]} {right}")


right = e("bsgz")


low = 0
high = 10**9

while low < high:
    mid = (low + high) // 2

    monkeys["humn"] = mid

    if e("lsbv"):
        high = mid
    else:
        low = mid + 1







