FILE = open('./input.txt')
SYMBOLS = ['@', '#', '$', '%', '&', '*', '-', '=', '+', '/']

grid = [list(line.strip()) for line in FILE if line.strip()]
locations: list[tuple[int, int]] = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell in SYMBOLS:
            for sub_y in range(y - 1, y + 2):
                for sub_x in range(x - 1, x + 2):
                    if grid[sub_y][sub_x].isdigit():
                        if sub_x > x - 1 and grid[sub_y][sub_x - 1].isdigit():
                            continue
                        locations.append((sub_y, sub_x))

numbers: list[int] = []

for location in locations:
    loc_y, loc_x = location
    num_str = ""

    x = loc_x
    while x >= 0:
        cell_val = grid[loc_y][x]
        if cell_val.isdigit():
            num_str = grid[loc_y][x] + num_str
            x -= 1
        else:
            break

    x = loc_x + 1
    while x < len(grid[0]):
        cell_val = grid[loc_y][x]
        if cell_val.isdigit():
            num_str = num_str + grid[loc_y][x]
            x += 1
        else:
            break

    if len(num_str) > 0:
        numbers.append(int(num_str))

sum = sum(numbers)
print(sum)