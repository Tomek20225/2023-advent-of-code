class Set:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class Game:
    def __init__(self, id, sets):
        self.id = id
        self.sets = sets

games = []
file = open('input.txt', 'r')

for line in file.readlines():
    id_str, sets_str = line.split(':')
    _, id = id_str.split()

    sets_split = sets_str.split(";")
    sets = []

    for set_str in sets_split:
        parts = [s.strip().split() for s in set_str.split(',')]
        r = 0
        g = 0
        b = 0

        for part in parts:
            num = int(part[0])
            color = part[1]

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