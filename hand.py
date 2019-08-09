import collections
import dataclasses


@dataclasses.dataclass(frozen = True)
class Card:
    suit: str
    value: str


class Hand(collections.UserList):
    pass


hand = Hand([
    Card('spades', '7'),
    Card('hearts', '3'),
    Card('diamonds', '3'),
    Card('clubs', 'A'),
    Card('hearts', 'K'),
])

for card in hand:
    print(card)

import random

print('rnd', random.choice(hand))

print(len(hand))
print(hand[0])

# iterator = iter(hand)
# while True:
#     item = next(iterator)
#     print(item)
