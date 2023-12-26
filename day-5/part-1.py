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
maps: dict[str, list[tuple[int, int, int]]] = {map:[] for map in KEYWORDS}
keyword_idx = 0

for line in LINES[1:]:
    if keyword_idx < len(KEYWORDS) and KEYWORDS[keyword_idx] in line:
        keyword_idx += 1
    elif line != "":
        dest_start, source_start, length = line.split(' ')
        maps[KEYWORDS[keyword_idx - 1]].append((int(source_start), int(dest_start), int(length)))

prev_property = "id"
for map_name, map in maps.items():
    property = PROPERTIES_MAP[map_name]
    
    for seed in seeds:
        prev_property_val = getattr(seed, prev_property)
        setattr(seed, property, prev_property_val)

        for source_start, dest_start, length in map:
            if source_start <= prev_property_val and prev_property_val < source_start + length:
                dist: int = prev_property_val - source_start
                setattr(seed, property, dest_start + dist)
                break

    prev_property = property

# Solution
lowest_location: int = sys.maxsize
for seed in seeds:
    if getattr(seed, 'location') < lowest_location:
        lowest_location = getattr(seed, 'location')

print(lowest_location)