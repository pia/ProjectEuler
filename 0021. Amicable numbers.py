# 0.17s user 0.01s system 95% cpu 0.187 total
from math import sqrt


def d(n):
    divs = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n / i)
    return sum(divs) - n


class Cache:
    """cache for d(n)"""

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 0
        elif n in self.cache:
            return self.cache[n]
        else:
            c = d(n)
            self.cache[n] = c
            return c


D = Cache()


def num_under(n):
    amicable = []
    for i in range(1, n):
        r = D(i)
        if D(r) == i and r != i:
            amicable.append(i)
    return amicable


print(sum(num_under(10000)))
