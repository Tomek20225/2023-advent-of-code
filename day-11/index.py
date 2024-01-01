from typing import TypeAlias

Cosmos: TypeAlias = list[list[str]]
Galaxy: TypeAlias = tuple[int, int] # (y, x)

GALAXY_CHAR = '#'
SPACE_CHAR = '.'

def expand_cosmos(galaxies: list[Galaxy], expansion_rate: int = 2) -> list[Galaxy]:
    expansion_rate -= 1

    cosmos_width, cosmos_height = -1, -1
    galaxies_list: list[list[int]] = []

    for galaxy in galaxies:
        if galaxy[0] > cosmos_height:
            cosmos_height = galaxy[0]
        if galaxy[1] > cosmos_width:
            cosmos_width = galaxy[1]
        galaxies_list.append(list(galaxy))
    cosmos_width += 1
    cosmos_height += 1

    rows_to_skip: list[int] = []
    
    # Expanding rows
    y = 0
    while y < cosmos_height:
        met_galaxy = False
        for x in range(0, cosmos_width):
            for galaxy_y, galaxy_x in galaxies_list:
                if galaxy_y == y and galaxy_x == x:
                    met_galaxy = True
                    break
        if not met_galaxy:
            for i in range(0, len(galaxies_list)):
                if galaxies_list[i][0] > y:
                    galaxies_list[i][0] += expansion_rate
            cosmos_height += expansion_rate
            rows_to_skip.append(y + 1)
            y += expansion_rate
        y += 1

    # Expanding cols
    x = 0
    while x < cosmos_width:
        met_galaxy = False
        y = 0
        while y < cosmos_height:
            if y in rows_to_skip:
                y += expansion_rate
                continue

            for galaxy_y, galaxy_x in galaxies_list:
                if galaxy_y == y and galaxy_x == x:
                    met_galaxy = True
                    break
            y += 1
        if not met_galaxy:
            for i in range(0, len(galaxies_list)):
                if galaxies_list[i][1] > x:
                    galaxies_list[i][1] += expansion_rate
            cosmos_width += expansion_rate
            x += expansion_rate
        x += 1
    
    return [tuple(galaxy) for galaxy in galaxies_list]

def get_galaxies(cosmos: Cosmos) -> list[Galaxy]:
    galaxies: list[Galaxy] = []
    for y, row in enumerate(cosmos):
        for x, cell in enumerate(row):
            if cell == GALAXY_CHAR:
                galaxies.append((y, x))
    return galaxies

def get_shortest_distance(start: Galaxy, end: Galaxy) -> int:
    if start == end:
        return 0

    distance = 0
    start = list(start)
    end = list(end)

    # No need to worry about going upwards
    # Since galaxies are sorted from top to bottom
    max_diagonal_skips = min(end[0] - start[0], abs(end[1] - start[1]))
    distance += max_diagonal_skips * 2
    start[0] += max_diagonal_skips
    start[1] += max_diagonal_skips * (1 if end[1] >= start[1] else -1)
    distance += abs(end[0] - start[0])
    distance += abs(end[1] - start[1])

    return distance

def get_distances(galaxies: list[Galaxy]) -> list[int]:
    distances: list[int] = []
    for i, galaxy_start in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            if i == j:
                continue
            galaxy_end = galaxies[j]
            distance = get_shortest_distance(galaxy_start, galaxy_end)
            distances.append(distance)
    return distances


# Preparation
FILE = open('./input.txt')
COSMOS_OBSERVED = [[char for char in line.strip()] for line in FILE if line.strip()]
GALAXIES_OBSERVED = get_galaxies(COSMOS_OBSERVED)


# Part 1
galaxies = expand_cosmos(GALAXIES_OBSERVED)
distances = get_distances(galaxies)
sum_of_distances = sum(distances)
print('Part 1:', sum_of_distances)


# Part 2
galaxies = expand_cosmos(GALAXIES_OBSERVED, 1_000_000)
distances = get_distances(galaxies)
sum_of_distances = sum(distances)
print('Part 2:', sum_of_distances)