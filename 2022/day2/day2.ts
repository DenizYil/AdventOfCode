import fs from 'fs'

type Move = "rock" | "paper" | "scissors"

const Item = (move: Move) => ({
    move,
    points: move === "rock" ? 1 : move === "paper" ? 2 : 3,
    beats: move === "rock" ? "scissors" : move === "paper" ? "rock" : "paper" as Move,
    lossesTo: move === "rock" ? "paper" : move === "paper" ? "scissors" : "rock" as Move
})

type ItemType = ReturnType<typeof Item>

const mapper: any = {
    A: Item("rock"),
    B: Item("paper"),
    C: Item("scissors"),
}

const findItem = (move: Move) => Object.values(mapper).find((item: any) => item.move === move) as ItemType

mapper["X"] = mapper.A 
mapper["Y"] = mapper.B
mapper["Z"] = mapper.C

const input = fs
    .readFileSync('./2022/day2/input.txt', 'utf-8')
    .split("\r\n")
    
const part1 = input
    .reduce((prev, current) => {

        const [opponentRaw, meRaw] = current.split(" ") as [keyof typeof mapper, keyof typeof mapper]

        const opponent = mapper[opponentRaw]
        const me = mapper[meRaw]
        
        prev += me.points;

        // Draw
        if (opponent.move === me.move) {
            return prev + 3
        }

        // Win
        if (me.beats === opponent.move) {
            return prev + 6
        }

        // Loss
        if (me.lossesTo === opponent.move) {
            return prev
        }

        return prev

    }, 0);

console.log(part1)

const part2 = input
    .reduce((prev, current) => {

        const [opponentRaw, meRaw] = current.split(" ") as [keyof typeof mapper, keyof typeof mapper]

        const opponent = mapper[opponentRaw] as ItemType
        const me = mapper[meRaw] as ItemType
        
        prev += 

        // I need to lose
        if (me.move === "rock") {
            const winsTo = findItem(opponent.beats)
            return prev + winsTo.points
        }

        // I need to draw
        if (me.move === "paper") {
            return prev + opponent.points
        }

        // I need to win
        if (me.move === "scissors") {
            const loseTo = findItem(opponent.beats)
            return prev + loseTo.points
        }

        return prev

    }, 0);

console.log(part2)





