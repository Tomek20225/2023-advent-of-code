# This is far from a efficient solution
#
# The algorithm should involve:
# - finding minimal ranges
# - skipping seeds which result in the same location number
# - or creating negative ranges and checking those
#
# This code should be treated more as a multiprocessing experiment
# For small numbers and ranges not creating the processes is much faster

import sys
import multiprocessing
from functools import partial
from typing import TypeAlias

Map: TypeAlias = list[tuple[int, int, int]]
Maps: TypeAlias = dict[str, Map]
Range: TypeAlias = tuple[int, int]

def process_range(range_tuple: Range, maps: Maps, properties: dict[str, str]) -> int:
    seed_range_start, seed_range_end = range_tuple
    lowest_location: int = sys.maxsize
    seed = {
        "id": 0,
        "soil": 0,
        "fertilizer": 0,
        "water": 0,
        "light": 0,
        "temperature": 0,
        "humidity": 0,
        "location": 0
    }

    for seed_id in range(seed_range_start, seed_range_end):
        prev_property = "id"
        seed['id'] = seed_id

        for map_name in maps:
            map = maps[map_name]
            property = properties[map_name]

            prev_property_val = seed[prev_property]
            seed[property] = prev_property_val

            for source_start, dest_start, length in map:
                if source_start <= prev_property_val and prev_property_val < source_start + length:
                    dist = prev_property_val - source_start
                    seed[property] = dest_start + dist
                    break

            prev_property = property

        if lowest_location > seed['location']:
            lowest_location = seed['location']
            print(f"Seed {seed_id} location {lowest_location}")

    return lowest_location


def process_wrapper(range_tuple: Range, maps: Maps, properties: dict[str, str]):
    return process_range(range_tuple, maps, properties)


def main() -> None:
    FILE = open('./input.txt')
    LINES = [line.strip() for line in FILE if line.strip()]
    KEYWORDS = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    PROPERTIES_MAP = {keyword:keyword.split('-')[2] for keyword in KEYWORDS}

    seed_descriptors: list[int] = [int(num) for num in LINES[0].split('seeds: ')[1].split(' ')]
    seed_ranges: list[Range] = [(seed_descriptors[i], seed_descriptors[i] + seed_descriptors[i+1]) for i in range(0, len(seed_descriptors), 2)]

    maps: Maps = {map:[] for map in KEYWORDS}
    keyword_idx = 0

    for line in LINES[1:]:
        if keyword_idx < len(KEYWORDS) and KEYWORDS[keyword_idx] in line:
            keyword_idx += 1
        elif line != "":
            dest_start, source_start, length = line.split(' ')
            maps[KEYWORDS[keyword_idx - 1]].append((int(source_start), int(dest_start), int(length)))

    with multiprocessing.Pool() as pool:
        partial_process_range = partial(process_wrapper, maps=maps, properties=PROPERTIES_MAP)
        results = pool.map(partial_process_range, seed_ranges)

    lowest_location = min(results)
    print(lowest_location)


if __name__ == '__main__':
    main()