let fs = require("fs")
let input = fs.readFileSync("input.txt").toString().split("\r\n")
let data = {}

for (let i = 0; i < input.length; i++) {
    let split = input[i].split(":")

    if (split[1].includes("*") || split[1].includes("+") || split[1].includes("-") || split[1].includes("/"))
    {
        data[split[0]] = split[1].trim()
    }
    else
    {
        data[split[0]] = parseInt(split[1].trim())
    }
}
function monkey(n) {
    m = data[n]


    try
    {
        // this will throw an error if m is a number!
        if (m.includes("*") || m.includes("+") || m.includes("-") || m.includes("/"))
        {
            let [a,b,c] = m.split(" ")

            a = monkey(a)
            c = monkey(c)

            if (b == "*")
            {
                return a * c
            }
            else if (b == "+")
            {
                return a + c
            }
            else if (b == "-")
            {
                return a - c
            }
            else if (b == "/")
            {
                return a / c
            }
        }
    }
    catch (e)
    {

    }

    return m

}

console.log("lccz")
console.log(monkey("lccz"))

console.log("pttp")
console.log(monkey("pttp"))

// idk what binary search is : D but this is it!
let nohuman = monkey("pttp")

start = 0
end = 10**20

console.log(end)

while (start < end)
{
    let mid = parseInt((start + end) / 2)
    data["humn"] = mid
    let s = nohuman - monkey("lccz")

    if (s < 0)
    {
        start = mid
    }
    if (s == 0) {
        console.log(mid)
        break
    }
    if (s > 0)
    {
        end = mid
    }
}
