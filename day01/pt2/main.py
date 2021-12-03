with open("./input.txt", "r") as file:
    lines = file.readlines()


d = {}

for line in lines:
    spl = line.split("  ")

    numb = int(spl[0])

    for c in spl[1:]:
        if not c or c == " " or not c.strip():
            continue

        if " " in c.strip():
            c = c.replace("\n", "")
            for i in c.split(" "):
                if i not in d:
                    d[i] = []
                d[i].append(numb)

            continue

        c = c.replace("\n", "").strip()

        if c not in d:
            d[c] = []

        d[c].append(numb)

count = 0
last = sum(d["A"])
d.pop("A")

for line in d:
    if last < sum(d[line]):
        count += 1
    last = sum(d[line])

print(count)