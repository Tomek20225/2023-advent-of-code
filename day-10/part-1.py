from typing import TypeAlias, Literal
from math import ceil

Location: TypeAlias = tuple[int, int] # (y, x)
Coords: TypeAlias = tuple[bool, bool, bool, bool]

FILE = open('./index.txt')
LINES = [line.strip() for line in FILE if line.strip()]
GRID = [[col for col in row] for row in LINES]
GRID_VISITED = [[False for _ in row] for row in LINES]
CONNECTION_MAP: dict[str, Coords] = {
    # TYPE: (CAN_NORTH, CAN_EAST, CAN_SOUTH, CAN_WEST)
    '|': (True, False, True, False),
    '-': (False, True, False, True),
    'L': (True, True, False, False),
    'J': (True, False, False, True),
    '7': (False, False, True, True),
    'F': (False, True, True, False),
    '.': (False, False, False, False),
    'S': (True, True, True, True),
}

def get_cell(loc: Location) -> str:
    y, x = loc
    return GRID[y][x]

def mark_visited(loc: Location) -> None:
    y, x = loc
    GRID_VISITED[y][x] = True

def is_visited(loc: Location) -> bool:
    y, x = loc
    return GRID_VISITED[y][x]

def is_move_possible(loc_a: Location, loc_b: Location) -> bool:
    y_a, x_a = loc_a
    y_b, x_b = loc_b

    cell_a = get_cell(loc_a)
    cell_b = get_cell(loc_b)

    moveset_a = CONNECTION_MAP[cell_a]
    moveset_b = CONNECTION_MAP[cell_b]

    # Checks movement from A to B
    # Moving north
    if y_a > y_b:
        return moveset_a[0] and moveset_b[2] and not is_visited(loc_b)
    # Moving east
    elif x_a < x_b:
        return moveset_a[1] and moveset_b[3] and not is_visited(loc_b)
    # Moving south
    elif y_a < y_b:
        return moveset_a[2] and moveset_b[0] and not is_visited(loc_b)
    # Moving west
    elif x_a > x_b:
        return moveset_a[3] and moveset_b[1] and not is_visited(loc_b)

    return False

def get_possible_moves(location: Location) -> list[Location]:
    y, x = location

    north_cell = (y - 1, x) if y - 1 >= 0 and is_move_possible(location, (y - 1, x)) else None
    east_cell = (y, x + 1) if x + 1 < len(GRID[0]) and is_move_possible(location, (y, x + 1)) else None
    south_cell = (y + 1, x) if y + 1 < len(GRID) and is_move_possible(location, (y + 1, x)) else None
    west_cell = (y, x - 1) if x - 1 >= 0 and is_move_possible(location, (y, x - 1)) else None
    
    possible_moves = [cell for cell in [north_cell, east_cell, south_cell, west_cell] if cell]
    return possible_moves

def move(loc_a: Location, loc_b: Location) -> Location | Literal[False]:
    # Gets location of the next location after loc_b
    mark_visited(loc_a)
    mark_visited(loc_b)

    y_a, x_a = loc_a
    y_b, x_b = loc_b

    cell_b = get_cell(loc_b)
    moveset_b = list(CONNECTION_MAP[cell_b])

    # Moving north
    if y_a > y_b:
        moveset_b[2] = False
    # Moving east
    elif x_a < x_b:
        moveset_b[3] = False
    # Moving south
    elif y_a < y_b:
        moveset_b[0] = False
    # Moving west
    elif x_a > x_b:
        moveset_b[1] = False
    
    next_move = moveset_b.index(True)
    next_loc = False

    match next_move:
        case 0:
            next_loc = (y_b - 1, x_b)
        case 1:
            next_loc = (y_b, x_b + 1)
        case 2:
            next_loc = (y_b + 1, x_b)
        case 3:
            next_loc = (y_b, x_b - 1)

    mark_visited(next_loc)
    return next_loc


# Part 1
start_location: Location
for y, row in enumerate(GRID):
    for x, cell in enumerate(row):
        if cell == 'S':
            start_location = (y, x)
            break

current_cell_loc = start_location
distance = 0

while True:
    current_cell = get_cell(current_cell_loc)
    if current_cell == 'S' and distance > 0:
        distance -= 1
        break

    possible_moves = get_possible_moves(current_cell_loc)
    passthrough_location = possible_moves[0]
    passthrough_cell = get_cell(passthrough_location)
    distance += 1
    if passthrough_cell == 'S':
        break

    next_location = move(current_cell_loc, passthrough_location)
    current_cell_loc = next_location
    distance += 1

distance = ceil(distance / 2)
print(distance)


# Part 2
# TODO: Implement a proper crawling algorithm. The code below doesn't work correctly
for row in GRID_VISITED:
    print(row)

y = 0
while y < len(GRID_VISITED):
    row = GRID_VISITED[y]
    x = 0
    while x < len(row):
        loc = (y, x)
        cell = is_visited(loc)
        if cell == False:
            mark_visited(loc)
            x += 1
        else:
            try:
                x = row.index(True, x + 1, len(row))
            except:
                x += 1
                continue
    y += 1

tiles = sum([len(row) - sum([int(cell) for cell in row]) for row in GRID_VISITED])
print('STOP')
for row in GRID_VISITED:
    print(row)
print(tiles)