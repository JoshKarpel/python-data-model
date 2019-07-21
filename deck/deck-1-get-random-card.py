import random

hand = [
    ('spades', '7'),
    ('hearts', '3'),
    ('diamonds', '3'),
    ('clubs', 'A'),
    ('hearts', 'K'),
]

for card in hand:
    suit, value = card
    print(f'Suit: {suit}, Value: {value}')

random_card = random.choice(hand)

print(f'\nRandom Card: {random_card}')
