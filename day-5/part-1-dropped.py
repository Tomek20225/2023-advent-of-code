# Dropped because this solution works well only with small numbers
# since it stores every possible mapping in memory
# The task input contains only large ints

import sys

class Seed:
    def __init__(self, id: int, soil: int = 0, fertilizer: int = 0, water: int = 0, light: int = 0, temperature: int = 0, humidity: int = 0, location: int = 0) -> None:
        self.id = id
        self.soil = soil
        self.fertilizer = fertilizer
        self.water = water
        self.light = light
        self.temperature = temperature
        self.humidity = humidity
        self.location = location

FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]
KEYWORDS = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
PROPERTIES_MAP = {keyword:keyword.split('-')[2] for keyword in KEYWORDS}

seeds = [Seed(id = int(num)) for num in LINES[0].split('seeds: ')[1].split(' ')]
maps: dict[str, list[tuple[int, int, int]]] = {map:{} for map in KEYWORDS}
keyword_idx = 0

for line in LINES[1:]:
    if keyword_idx < len(KEYWORDS) and KEYWORDS[keyword_idx] in line:
        keyword_idx += 1
    elif line != "":
        dest_start, source_start, length = line.split(' ')
        for i in range(0, int(length)):
            maps[KEYWORDS[keyword_idx - 1]][int(source_start) + i] = int(dest_start) + i

prev_property = "id"
for map in KEYWORDS:
    property = PROPERTIES_MAP[map]
    
    for seed in seeds:
        prev_property_val = seed[prev_property]
        try:
            seed[property] = maps[map][prev_property_val]
        except:
            seed[property] = seed[prev_property]

    prev_property = property

# Solution
lowest_location: int = sys.maxsize
for seed in seeds:
    if seed['location'] < lowest_location:
        lowest_location = seed['location']

print(lowest_location)