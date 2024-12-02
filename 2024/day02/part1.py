with open("./input.txt", "r") as file:
	lines = [line.strip() for line in file.readlines()]

ans = 0

for line in lines:
	nums = list(int(num) for num in line.split(" "))

	prev = nums[0]
	unsafe = False
	decreasing = nums[0] > nums[1]

	for num in nums[1:]:
		if decreasing and num > prev:
			unsafe = True
			break

		if not decreasing and num < prev:
			unsafe = True
			break

		if num == prev:
			unsafe = True
			break

		if abs(num - prev) > 3:
			unsafe = True
			break
		prev = num
	
	if not unsafe:
		ans += 1

print(ans)