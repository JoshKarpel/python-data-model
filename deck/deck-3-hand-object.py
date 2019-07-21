import random
import dataclasses


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)


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

random_card = random.choice(hand.cards)

print(f'\nRandom Card: {random_card}')
