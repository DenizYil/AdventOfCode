const fs = require('fs')

const input = fs.readFileSync('./input.txt', 'utf8')

const matches = input.matchAll(/mul\([^()]*?\)/gm)

let ans = 0
let i = 0

const a =[...matches]

a.forEach(element => {
	element = element[0].substring(3).replace("(", "").replace(")", "")
	const [a, b] = element.split(",")

	console.log(a, b)

	if (Number.isNaN(parseInt(a)) || Number.isNaN(parseInt(b))) return

	ans += parseInt(a) * parseInt(b)
});

console.log(ans)