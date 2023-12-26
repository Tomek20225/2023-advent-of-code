from functools import cmp_to_key
from typing import TypeAlias

LABELS = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1}
TYPES = {'5OK':7, '4OK':6, 'FH':5, '3OK':4, '2P':3, '1P':2, 'H':1, 'O':0}
Hand: TypeAlias = tuple[str, int, str]

FILE = open('./input.txt')

def categorize_hand(hand: str) -> str:
    counter = {}

    for label in hand:
        if label in counter:
            counter[label] += 1
        else:
            counter[label] = 1

    counter = dict(sorted(counter.items(), key=lambda x:x[1], reverse=True))
    labels = list(counter.keys())
    label_count = len(counter)

    type = TYPES["O"]

    if label_count == 1:
        type = '5OK'
    elif label_count == 2:
        if counter[labels[0]] == 4 or counter[labels[1]] == 4:
            type = '4OK'
        elif counter[labels[0]] == 3 and counter[labels[1]] == 2:
            type = 'FH'
    elif label_count == 3:
        if counter[labels[0]] == 3 and counter[labels[1]] == 1:
            type = '3OK'
        elif counter[labels[0]] == 2 and counter[labels[1]] == 2:
            type = '2P'
    elif label_count == 4:
        if counter[labels[0]] == 2 and counter[labels[1]] == 1 and counter[labels[2]] == 1:
            type = '1P'
    elif label_count == 5:
        type = 'H'

    if 'J' not in labels:
        return type

    joker_count: int = counter['J']

    if joker_count >= 4:
        return '5OK'
    elif joker_count == 3:
        if type == 'FH':
            return '5OK'
        elif type == '3OK':
            return '4OK'
    elif joker_count == 2:
        if type == 'FH':
            return '5OK'
        elif type == '2P':
            return '4OK'
        elif type == '1P':
            return '3OK'
    elif joker_count == 1:
        if type == '4OK':
            return '5OK'
        elif type == '3OK':
            return '4OK'
        elif type == '2P':
            return 'FH'
        elif type == '1P':
            return '3OK'
        elif type == 'H':
            return '1P'

    return type

def process_hand(str: str) -> Hand:
    hand, bid = str.strip().split(' ')
    bid = int(bid)
    return (hand, bid, categorize_hand(hand))

def compare_hands(hand_a: Hand, hand_b: Hand) -> int:
    a = TYPES[hand_a[2]]
    b = TYPES[hand_b[2]]

    if a > b:
        return -1
    elif a == b:
        for i in range(0, len(hand_a[0])):
            la = LABELS[hand_a[0][i]]
            lb = LABELS[hand_b[0][i]]
            if la > lb:
                return -1
            elif la < lb:
                return 1
        return 0
    else:
        return 1


cmp_fn = cmp_to_key(compare_hands)

hands = [process_hand(line) for line in FILE if line.strip()]
hands = sorted(hands, key=cmp_fn)

# Solution
winnings = 0
for i, hand in enumerate(hands):
    rank = len(hands) - i
    winnings += hand[1] * rank

print(winnings)