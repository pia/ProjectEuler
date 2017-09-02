def not_divisible(n):
    return lambda x: x % n > 0


def odd_list():
    n = 1
    while True:
        n += 2
        yield n


def primes(end_num):
    li = odd_list()
    yield 2
    while True:
        n = next(li)
        if n > end_num:
            break
        yield n
        li = filter(not_divisible(n), li)


print(list(primes(105930))[10000])
