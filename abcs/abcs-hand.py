import dataclasses
import random


@dataclasses.dataclass()
class Card:
    suit: str
    value: str


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)

    def __getitem__(self, item):
        return self.cards[item]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        yield from self.cards

    def __contains__(self, item):
        return item in self.cards

    def __reversed__(self):
        yield from reversed(self.cards)

    def pop(self):
        return self.cards.pop()

    def extend(self, iterable):
        self.cards.extend(iterable)

    def remove(self, item):
        self.cards.remove(item)

    def __str__(self):
        return f'Hand({self.cards})'


hand = Hand(
    Card(suit, value) for suit, value in
    (('spades', '7'),
     ('hearts', '3'),
     ('diamonds', '3'),)
)
print(hand)

hand.extend([('clubs', 'A'), ('hearts', 'K')])
print(hand)

card = hand.pop()
print(card)
print(hand)

print(Card('spades', '7') in hand)

print(random.choice(hand))
