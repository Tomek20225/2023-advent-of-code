file = open('./input.txt')
lines = [line.strip() for line in file if line.strip()]

time = int("".join([num for num in lines[0].replace('Time:', '').split(' ') if num]))
dist = int("".join([num for num in lines[1].replace('Distance:', '').split(' ') if num]))

starts_winning_at = 0
ends_winning_at = time

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