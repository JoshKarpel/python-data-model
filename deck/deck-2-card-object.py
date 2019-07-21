import random
import dataclasses


@dataclasses.dataclass()
class Card:
    suit: str
    value: str


hand = [
    Card(suit, value) for suit, value in
    (('spades', '7'),
     ('hearts', '3'),
     ('diamonds', '3'),
     ('clubs', 'A'),
     ('hearts', 'K'),)
]

for card in hand:
    print(f'Suit: {card.suit}, Value: {card.value}')

random_card = random.choice(hand)

print(f'\nRandom Card: {random_card}')
