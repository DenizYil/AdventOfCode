with open("./input.txt", "r") as file:
	lines = [line.strip() for line in file.readlines()]

line = "".join(lines).split("mul")
print(line)
ans = 0

dont = False
justnow = False

for pair in line:
	if "(" not in pair and ")" not in pair:
		continue

	print("Pair:", pair)

	if "don't()" in pair:
		justnow = True
		dont = True

		print("Don't do it!")

	if dont and "do()" in pair:
		dont = False
		continue

	if dont and not justnow:
		print("Skipping", pair)
		continue

	if dont and justnow:
		justnow = False

	cancel = False

	a = ""
	b = ""

	for char in pair[1:]:
		if char == ",":
			break

		a += char

	if not a.isdigit():
		continue

	for char in pair[len(a)+2:]:
		if char == ")":
			break

		if not char.isdigit():
			cancel = True
			break

		b += char
		
	if cancel:
		continue
	print("Adding", a, "*", b)
	ans += int(a) * int(b)

print(ans)