import random

START_SEQUENCES = {
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'blue': '\u001b[34m',
}
RESET_SEQUENCE = '\u001b[0m'


# print(START_SEQUENCES['green'], end = '')
# print('Hello world, but green!')
# print(RESET_SEQUENCE, end = '')
# print("Not green!")


class Colorizer:
    def __init__(self, color):
        self.color = color

    def _print_start_sequence(self):
        print(START_SEQUENCES[self.color], end = '')

    def __enter__(self):
        self._print_start_sequence()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(RESET_SEQUENCE, end = '')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == 'color':
            self._print_start_sequence()

    def __invert__(self):
        self.color = random.choice(list(START_SEQUENCES.keys()))


with Colorizer('green') as colorizer:
    print('Hello world, but green!')
    colorizer.color = 'red'
    print('red!')
    colorizer.color = 'green'
    print('green!')
    for _ in range(5):
        # do something
        ~colorizer
        print('random')
print("Not green!")
