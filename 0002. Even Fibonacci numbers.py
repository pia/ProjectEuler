def fibs(maxValue, a=1, b=2):
    fib = [a, b]
    while True:
        a, b = b, a + b
        if b <= maxValue:
            fib.append(b)
        else:
            return fib


print(sum([x for x in fibs(4000000) if x % 2 == 0]))
