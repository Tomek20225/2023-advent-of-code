file = open('./input.txt')

symbol = '*'
grid = [list(line.strip()) for line in file]
locations = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == symbol:
            temp_locations = []
            
            for sub_y in range(y - 1, y + 2):
                for sub_x in range(x - 1, x + 2):
                    if grid[sub_y][sub_x].isdigit():
                        if sub_x > x - 1 and grid[sub_y][sub_x - 1].isdigit():
                            continue
                        temp_locations.append((sub_y, sub_x))
            
            if len(temp_locations) == 2:
                locations.append((temp_locations[0], temp_locations[1]))


def get_num(location):
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
        return int(num_str)
    else:
        return False


numbers = []

for location_pair in locations:
    loc_1, loc_2 = location_pair
    num_1 = get_num(loc_1)
    num_2 = get_num(loc_2)
    ratio = num_1 * num_2
    numbers.append(ratio)

print(sum(numbers))