import functools

file = open('./input.txt')
lines = [line.strip() for line in file if line.strip()]

times = [int(num) for num in lines[0].replace('Time:', '').split(' ') if num]
distances = [int(num) for num in lines[1].replace('Distance:', '').split(' ') if num]
races = [(times[i], distances[i]) for i in range(0, len(times))]

races_optimized = []
for race in races:
    time, win_dist = race
    winning_hold_times = []

    for hold_ms in range(1, time):
        speed = hold_ms
        remaining_time = time - hold_ms
        travelled_dist = remaining_time * speed
        if travelled_dist > win_dist:
            winning_hold_times.append(hold_ms)

    races_optimized.append(winning_hold_times)

winning_ways = functools.reduce(lambda a, b: a * len(b), races_optimized, 1)
print(winning_ways)