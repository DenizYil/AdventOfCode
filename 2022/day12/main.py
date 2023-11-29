import string
from igraph import Graph

ALPHABET = list(string.ascii_lowercase)
print(ALPHABET)

with open("./input.txt", "r") as file:
    lines = [list(line.strip()) for line in file.read().split("\n")]
    print(lines)



graph = Graph()

for row in range(len(lines)):
    for col in range(len(lines[row])):
        item = lines[row][col]



graph.get_shortest_paths()
