# f(x)  =  x^2 + x
# g(x)  =  x^3 + 2x^2 + 1
# h(x)  =  f(x) + g(x)  =  1x^3 + 3x^2 + 1x^1 + 1x^0
#                          3:1    2:3    1:1    0:1
import itertools


class Polynomial:
    def __init__(self, powers_to_coefficient):
        self._powers_to_coefficients = powers_to_coefficient

    @property
    def powers_and_coefficients(self):
        yield from self._powers_to_coefficients.items()

    def __str__(self):
        return ' + '.join(
            f'{coefficient}x^{power}'
            for power, coefficient
            in self.powers_and_coefficients
        )

    def __call__(self, x):
        return sum(
            coefficient * (x ** power)
            for power, coefficient
            in self.powers_and_coefficients
        )

    def __getitem__(self, power):
        return self._powers_to_coefficients[power]

    def get(self, power, default = 0):
        return self._powers_to_coefficients.get(power, default)

    def __add__(self, other):
        powers = itertools.chain(self._powers_to_coefficients.keys(), other._powers_to_coefficients.keys())

        poly = Polynomial(
            {p: self.get(p) + other.get(p)
             for p in powers}

        )

        return poly


f = Polynomial({2: 1, 1: 1})
print(f)
print(f(5))
g = Polynomial({3: 1, 2: 2, 0: 1})

print(f + g)
