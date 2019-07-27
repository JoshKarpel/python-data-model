# x + x^2
# x^3 + 2x^2 + 1
# sum: x^3 + 3x^2 + 1x^1 + 1 x^0
#      3:1     2:3     1:1    0:1

import collections
import itertools


class Polynomial:
    def __init__(self, coefficients = None):
        if coefficients is None:
            coefficients = {}
        self.powers_to_coefficients = collections.defaultdict(int)
        self.powers_to_coefficients.update(coefficients)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.powers_to_coefficients})'

    def __str__(self):
        parts = (f'{coefficient}x^{power}' for power, coefficient in self.powers_and_coefficients())
        return ' + '.join(parts)

    def powers_and_coefficients(self):
        yield from sorted(self.powers_to_coefficients.items(), reverse = True)

    def __getitem__(self, key):
        return self.powers_to_coefficients[key]

    def __setitem__(self, key, value):
        self.powers_to_coefficients[key] = value

    def __add__(self, other):
        new = self.__class__()
        for power, coefficient in itertools.chain(self.powers_and_coefficients(), other.powers_and_coefficients()):
            new[power] += coefficient

        return new

    def __sub__(self, other):
        return NotImplemented

    def __call__(self, x):
        return sum(coefficient * (x ** power) for power, coefficient in self.powers_and_coefficients())

    def __len__(self):
        return len(self.powers_to_coefficients)

a = Polynomial({3: 1, 2: 3, 1: 1, 0: 1})
print(a)
b = Polynomial({4: 2, 2: -3, 0: -4})
print(a)

s = a + b
print(s)

s[10] = 5
print(s)

print(s(1))
