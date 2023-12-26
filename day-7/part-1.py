from functools import cmp_to_key
from typing import TypeAlias, Literal

LABELS = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
TYPES = {'5OK':7, '4OK':6, 'FH':5, '3OK':4, '2P':3, '1P':2, 'H':1, 'O':0}
Hand: TypeAlias = tuple[str, int, str]

FILE = open('./input.txt')

def categorize_hand(hand: str) -> str:
    counter: dict[str, int] = {}

    for label in hand:
        if label in counter:
            counter[label] += 1
        else:
            counter[label] = 1

    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    labels = list(counter.keys())
    label_count = len(counter)

    match label_count:
        case 1:
            return '5OK'
        case 2:
            if counter[labels[0]] == 4 or counter[labels[1]] == 4:
                return '4OK'
            elif counter[labels[0]] == 3 and counter[labels[1]] == 2:
                return 'FH'
        case 3:
            if counter[labels[0]] == 3 and counter[labels[1]] == 1:
                return '3OK'
            elif counter[labels[0]] == 2 and counter[labels[1]] == 2:
                return '2P'
        case 4:
            if counter[labels[0]] == 2 and counter[labels[1]] == 1 and counter[labels[2]] == 1:
                return '1P'
        case 5:
            return 'H'

    return TYPES[-1]

def process_hand(str: str) -> Hand:
    hand, bid = str.strip().split(' ')
    return (hand, int(bid), categorize_hand(hand))

def compare_hands(hand_a: Hand, hand_b: Hand) -> Literal[-1, 0, 1]:
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