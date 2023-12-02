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


ans = list("" for item in lines)

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char.isnumeric():
            ans[i] += char
        for k, v in transformer.items():
            try:
                if line[j:j+len(k)] == k:
                    ans[i] += v
            except IndexError:
                pass


print(ans)
print(sum(int(x[0] + x[-1]) for x in ans))