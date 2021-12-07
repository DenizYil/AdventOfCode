from typing import List
from copy import copy


with open("./input.txt") as file:
    lines = [line for line in file.readlines()]

numbersToMark = [int(number) for number in lines[0].split(",")]
marked = []

lines = lines[2:]

class Mark:
    def __init__(self, number: int) -> None:
        self.number = number
        self.marked = False

    def __repr__(self) -> str:
        return f"number={self.number}, marked={self.marked}"

class Board:
    def __init__(self, marks: List[List[Mark]]) -> None:
        self.marks = marks

    def __repr__(self) -> str:
        return f"{self.marks}"

    def mark(self, number: int):
        for row in self.marks:
            for mark in row:
                if number == mark.number:
                    mark.marked = True

    def has_won(self) -> bool:
        # Rows
        for row in self.marks:
            won = True

            for mark in row:
                if not mark.marked:
                    won = False
                    break
            
            if won:
                return True

        # Columns
        for i in range(len(self.marks)):
            won = True
            for row in self.marks:
                if not row[i].marked:
                    won = False
                    break
            if won:
                return True

        return False

    def sum(self) -> int:
        sum = 0
        for row in self.marks:
            for mark in row:
                if not mark.marked:
                    sum += mark.number

        return sum


boards: List[Board] = []
marks: List[List[Mark]] = []

for line in lines:
    if line != "\n":
        line = line.replace("  ", " ").strip()

        row = []

        for numb in line.split(" "):
            mark = Mark(int(numb))
            row.append(mark)

        marks.append(row)

    else:
        boards.append(Board(marks))
        marks = []

# Last one
boards.append(Board(marks))

def main():
    for mark in numbersToMark:
        for board in copy(boards):
            board.mark(mark)

            if board.has_won():
                boards.remove(board)
            
            if not boards:
                print("BOARD HAS WON", board.sum() )
                print("Multiplied:", board.sum() * mark)
                return
            

main()