import functools 

class Card:
    def __init__(self, winning_nums, set_nums, instances = 1, matches = 0, score = 0):
        self.winning_nums = winning_nums
        self.set_nums = set_nums
        self.instances = instances
        self.matches = matches
        self.score = score

file = open('./input.txt')
cards = []

for line in file:
    all_nums = line.split(':')[1].strip()
    all_nums_split = all_nums.split('|')
    winning_nums = [int(num) for num in all_nums_split[0].strip().split(' ') if num]
    set_nums = [int(num) for num in all_nums_split[1].strip().split(' ') if num]

    matches = functools.reduce(lambda a, b: a + 1 if b in winning_nums else a, set_nums, 0)
    score = pow(2, matches - 1) if matches > 0 else 0

    cards.append(Card(
        winning_nums,
        set_nums,
        1,
        matches,
        score
    ))

# Part 1
final_score = functools.reduce(lambda a,  b: a + b.score, cards, 0)
print(f"Part 1: {final_score}")

# Part 2
total_cards = 0
for i in range(0, len(cards)):
    card = cards[i]

    if card.matches > 0:
        for j in range(i + 1, i + card.matches + 1):
            cards[j].instances += card.instances

    total_cards += card.instances

print(f"Part 2: {total_cards}")