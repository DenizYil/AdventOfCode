with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    
ans = 0
left, right = [], []

for line in lines:
	s = line.split(" ")
	left.append(int(s[0].strip()))
	right.append(int(s[-1].strip()))
	
for item in left:
	ans += item * right.count(item)

print(ans)
