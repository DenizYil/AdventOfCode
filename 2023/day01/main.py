with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

transformer = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

p1, p2 = [[""] * len(lines)] * 2

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char.isnumeric():
            p1[i] += char
            p2[i] += char
        for k, v in transformer.items():
            try:
                if line[j:j+len(k)] == k:
                    p2[i] += v
            except IndexError:
                pass

print(sum(int(x[0] + x[-1]) for x in p1))
print(sum(int(x[0] + x[-1]) for x in p2))
