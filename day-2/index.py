class Set:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

class Game:
    def __init__(self, id: int, sets: list[Set]) -> None:
        self.id = id
        self.sets = sets

FILE = open('input.txt', 'r')

games: list[Game] = []

for line in FILE.readlines():
    id_str, sets_str = line.split(':')
    _, id = id_str.split()

    sets_split = sets_str.split(";")
    sets: list[Set] = []

    for set_str in sets_split:
        parts = [s.strip().split() for s in set_str.split(',')]
        r = 0
        g = 0
        b = 0

        for num, color in parts:
            num = int(num)

            if "red" == color:
                r = num
            elif "green" == color:
                g = num
            elif "blue" == color:
                b = num

        sets.append(Set(r, g, b))

    games.append(Game(int(id), sets))


# Part 1
sum = 0

for game in games:
    possible = True

    for set in game.sets:
        if set.red > 12 or set.green > 13 or set.blue > 14:
            possible = False
            break

    if possible:
        sum += game.id

print("Part 1:", sum)


# Part 2
sum = 0

for game in games:
    maxRed = 0
    maxGreen = 0
    maxBlue = 0

    for set in game.sets:
        if set.red > maxRed:
            maxRed = set.red
        if set.green > maxGreen:
            maxGreen = set.green
        if set.blue > maxBlue:
            maxBlue = set.blue

    power = maxRed * maxGreen * maxBlue
    sum += power

print("Part 2:", sum)