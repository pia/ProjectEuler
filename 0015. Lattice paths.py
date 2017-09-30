from math import factorial


def c(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def lattice_paths(x, y):
    return c(x + y, x)


print(lattice_paths(20, 20))
