with open("./input.txt", "r") as file:
	lines = [line.strip() for line in file.readlines()]

ans = 0
left, right = [], []

for line in lines:
	s = line.split(" ")
	left.append(int(s[0].strip()))
	right.append(int(s[-1].strip()))
	
while len(left):
	l = min(left)
	r = min(right)

	ans += abs(l - r)
	left.remove(l)
	right.remove(r)

print(ans)
