import functools
from typing import TypeAlias

FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]

times = [int(num) for num in LINES[0].replace('Time:', '').split(' ') if num]
distances = [int(num) for num in LINES[1].replace('Distance:', '').split(' ') if num]
races: list[tuple[int, int]] = [(times[i], distances[i]) for i in range(0, len(times))]

races_optimized: list[list[int]] = []

for race in races:
    time, win_dist = race
    winning_hold_times: list[int] = []

    for hold_ms in range(1, time):
        speed = hold_ms
        remaining_time = time - hold_ms
        travelled_dist = remaining_time * speed
        if travelled_dist > win_dist:
            winning_hold_times.append(hold_ms)

    races_optimized.append(winning_hold_times)

winning_ways = functools.reduce(lambda a, b: a * len(b), races_optimized, 1)
print(winning_ways)