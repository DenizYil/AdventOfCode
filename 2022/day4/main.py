def to_int(arr):
    return [int(a) for a in arr]

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [line.split(",") for line in lines]
    lines = [(to_int(a.split("-")), to_int(b.split("-"))) for a, b in lines]

def part_one():
    ans = 0
    for a, b in lines:
        if a[0]<= b[0] and a[1] >= b[1]:
            ans += 1
        elif a[0] >= b[0] and a[1] <= b[1]:
            ans += 1
    
    return ans

def part_two():
    ans = 0
    for a, b  in lines:
        aS = set(range(a[0], a[1]+1))
        bS = set(range(b[0], b[1]+1))

        inter = aS.intersection(bS)

        if inter:
            ans += 1

    return ans


print(part_one())
print(part_two())