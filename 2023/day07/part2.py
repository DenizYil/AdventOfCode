from functools import cmp_to_key
from enum import Enum

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [(line.split()[0], int(line.split()[1])) for line in lines]

class PokerType(Enum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

def count_unique(cards):
    return len(set(cards))

def get_poker_type(c):
    chars = list(c[0])
    card = sorted(chars, key=lambda char: ord(char))
    chars = list(card)
    card = sorted(chars, key=lambda char: chars.count(char), reverse=True)

    real_card = card

    merged = "".join(card)

    saves = []

    for char in real_card:
        _type = None
        card = list(merged.replace("J", char))
        chars = list(card)
        card = sorted(chars, key=lambda char: ord(char))
        chars = list(card)
        card = sorted(chars, key=lambda char: chars.count(char), reverse=True)

        if count_unique(card) == 1:
            _type = PokerType.FiveOfAKind
        elif count_unique(card[:4]) == 1:
            _type = PokerType.FourOfAKind
        elif count_unique(card[:3]) == 1 and count_unique(card[3:5]) == 1:
            _type = PokerType.FullHouse
        elif count_unique(card[:3]) == 1:
            _type = PokerType.ThreeOfAKind
        elif count_unique(card[:2]) == 1 and count_unique(card[2:4]) == 1:
            _type = PokerType.TwoPair
        elif count_unique(card[:2]) == 1:
            _type = PokerType.OnePair
        else:
            _type = PokerType.HighCard

        saves.append(_type)

    _type = max([s.value for s in saves])
    print(c[0], PokerType(_type), saves)

    return (PokerType(_type), "".join(card), c[0], c[1])


def comp(n1, n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0

def get_score(char):
    if char.isdigit():
        return int(char)

    if char == "A":
        return 14
    if char == "K":
        return 13
    if char == "Q":
        return 12
    if char == "T":
        return 10
    if char == "J":
        return 1

def compare(c1, c2):
    (c1_type, _, c1_card, _) = c1
    (c2_type, _, c2_card, _) = c2

    if c1_type.value > c2_type.value:
        return 1

    if c1_type.value < c2_type.value:
        return -1

    for i in range(len(c1_card)):
        c1_c = c1_card[i]
        c2_c = c2_card[i]

        if c1_c != c2_c:
            return comp(get_score(c1_c), get_score(c2_c))


lines = [get_poker_type(card) for card in lines]


items = sorted(lines, key=cmp_to_key(compare))
ans = []
for i, (_, _, card, bid) in enumerate(items, 1):
    ans.append(i * bid)

print(sum(ans))
