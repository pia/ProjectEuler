for m in range(22, 0, -1):
    if 500 % m == 0:
        n = 500 / m - m
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a > 0 and b > 0 and c > 0:
            print(a * b * c)
