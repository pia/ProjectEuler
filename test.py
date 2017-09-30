from math import pow, sqrt


def fib(n):
    up = pow(1 + sqrt(5), n) - pow(1 - sqrt(5), n)
    down = pow(2, n) * sqrt(5)
    return up // down

index = 1
while True:
    index += 1
    if fib(index) > 10**999:
        print(index)