FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]

time = int(LINES[0].replace('Time:', '').replace(' ', ''))
dist = int(LINES[1].replace('Distance:', '').replace(' ', ''))

starts_winning_at: int = 0
ends_winning_at: int = time

for hold_ms in range(0, time):
    speed = hold_ms
    remaining_time = time - hold_ms
    travelled_dist = remaining_time * speed
    if travelled_dist > dist:
        starts_winning_at = hold_ms
        break

for hold_ms in range(time, starts_winning_at, -1):
    speed = hold_ms
    remaining_time = time - hold_ms
    travelled_dist = remaining_time * speed
    if travelled_dist > dist:
        ends_winning_at = hold_ms
        break


winning_ways = ends_winning_at - starts_winning_at + 1
print(winning_ways)