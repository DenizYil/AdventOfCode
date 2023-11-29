import math

with open("./input.txt", "r") as file:
    lines = [l.strip() for l in file.read().split("\n\n")]


swagger = 0

def parse(s_arr, pointer=0):
    arr = []

    while pointer != len(s_arr):
        char = s_arr[pointer]

        if char == "[":
            new, pointer = parse(s_arr, pointer+1)
            arr.append(new)
            continue
        elif char == "]":
            return (arr, pointer+1)
        elif char.isnumeric():
            arr.append(int(char))

        pointer += 1

    return (arr[0], pointer)


def compare(left, right):
    global swagger

    debug = swagger == 4

    if debug:
        print(left, right)

    i = 0


    while True:
        try:
            l = left[i]
        except IndexError:
            return True

        try:
            r = right[i]
        except IndexError:
            return False


        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                return False


        elif isinstance(l, list) and isinstance(r, list):
            return compare(l, r)

        else:
            comp = None

            if not isinstance(l, list):
                comp = compare([l], r)
            else:
                comp = compare(l, [r])

            return comp

        i += 1

    return True


actual = []
for i, pairs in enumerate(lines):
    left, right = pairs.split("\n")
    left = parse(left)
    right = parse(right)

    swagger = i

    nice = compare(left, right)
    actual.append(nice)


expected = [True, True, False, True, False, True, False, False]

print(expected)
print(actual)