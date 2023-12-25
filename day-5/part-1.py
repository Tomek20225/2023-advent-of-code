import sys

file = open('./input.txt')
lines = [line.strip() for line in file if line.strip()]
keywords = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

seeds = []
for num in lines[0].split('seeds: ')[1].split(' '):
    seeds.append({
        "id": int(num),
        "soil": 0,
        "fertilizer": 0,
        "water": 0,
        "light": 0,
        "temperature": 0,
        "humidity": 0,
        "location": 0
    })

maps = {map:[] for map in keywords}

keyword_idx = 0

for line in lines[1:]:
    if keyword_idx < len(keywords) and keywords[keyword_idx] in line:
        keyword_idx += 1
    elif line != "":
        dest_start, source_start, length = line.split(' ')
        maps[keywords[keyword_idx - 1]].append((int(source_start), int(dest_start), int(length)))

prev_property = "id"
for map_name, map in maps.items():
    property = map_name.split('-')[2]
    
    for seed in seeds:
        prev_property_val = seed[prev_property]
        seed[property] = prev_property_val

        for source_start, dest_start, length in map:
            if source_start <= prev_property_val and prev_property_val < source_start + length:
                dist = prev_property_val - source_start
                seed[property] = dest_start + dist
                break

    prev_property = property

# Solution
lowest_location = sys.maxsize
for seed in seeds:
    if seed['location'] < lowest_location:
        lowest_location = seed['location']
print(lowest_location)