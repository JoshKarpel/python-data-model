import random
import dataclasses


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)

    def score(self):
        return 5

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        yield from self.cards

    def add_card(self, card):
        self.cards.append(card)

    def pop_random(self):
        idx = random.randint(0, len(self))
        return self.cards.pop(idx)

    def __iadd__(self, other):
        if isinstance(other, Card):
            self.cards.append(other)
        else:
            self.cards.extend(other)
        return self


@dataclasses.dataclass()
class Card:
    suit: str
    value: str


hand = Hand(
    Card(suit, value) for suit, value in
    (('spades', '7'),
     ('hearts', '3'),
     ('diamonds', '3'),
     ('clubs', 'A'),
     ('hearts', 'K'),)
)

for card in hand.cards:
    print(f'Suit: {card.suit}, Value: {card.value}')

random_card = random.choice(hand)

print(f'\nRandom Card: {random_card}')

print(hand.score())
print(hand[3])
print(len(hand))

hand.cards.append(Card('spades', '8'))
print(len(hand))

hand.add_card(Card('spades', '6'))
print(len(hand))
print(hand[-1])

hand += [Card('hearts', '2'), Card('hearts', '1')]
hand += Card('hearts', '2')
print(hand[-1])
print(len(hand))

for card in hand:
    print(card)
