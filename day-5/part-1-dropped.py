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

maps = {map:{} for map in keywords}
keyword_idx = 0

for line in lines[1:]:
    if keyword_idx < len(keywords) and keywords[keyword_idx] in line:
        keyword_idx += 1
    elif line != "":
        dest_start, source_start, length = line.split(' ')
        for i in range(0, int(length)):
            maps[keywords[keyword_idx - 1]][int(source_start) + i] = int(dest_start) + i

prev_property = "id"
for map in keywords:
    property = map.split('-')[2]
    
    for seed in seeds:
        prev_property_val = seed[prev_property]
        try:
            seed[property] = maps[map][prev_property_val]
        except:
            seed[property] = seed[prev_property]

    prev_property = property

# Solution
lowest_location = sys.maxsize
for seed in seeds:
    if seed['location'] < lowest_location:
        lowest_location = seed['location']
print(lowest_location)

# Dropped because this solution works well only with small numbers
# The task input contained only large ints