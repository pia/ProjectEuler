from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def smallest_multiple(n):
    def lcm(a, b):
        return a * b / gcd(a, b)

    return reduce(lcm, range(1, 21))


print(smallest_multiple(20))
