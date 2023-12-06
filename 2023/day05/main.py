import math
from collections import defaultdict

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    _seeds = list(int(x) for x in lines[0].split(": ")[1].split(" "))

    seeds, soils, fertilizers, water, light, temperature, humidity = {}, {}, {}, {}, {}, {}, {}

    add_to = None
    for line in lines[1:]:
        if "seed-to-soil" in line:
            add_to = seeds
        elif "soil-to-fertilizer" in line:
            add_to = soils
        elif "fertilizer-to-water" in line:
            add_to = fertilizers
        elif "water-to-light" in line:
            add_to = water
        elif "light-to-temperature" in line:
            add_to = light
        elif "temperature-to-humidity" in line:
            add_to = temperature
        elif "humidity-to-" in line:
            add_to = humidity
        else:
            if line:
                items = line.split(" ")
                add_to[int(items[1])] = (int(items[0]), int(items[2]))


converters = [seeds, soils, fertilizers, water, light, temperature, humidity]
ans = []

for i, seed in enumerate(_seeds):
    print(f"Seed {i+1}/{len(_seeds)}: {seed}")

    for converter in converters:
        scanner = None

        for source, (destination, _range) in converter.items():
            if source <= seed < source + _range:
                scanner = (source, destination, _range)
                seed = destination + (seed - source)
                break

    ans.append(seed)


print(ans)
print(min(ans))