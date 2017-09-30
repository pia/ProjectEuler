from math import sqrt
import time

tic = time.time()


def abundants(n):
    res = []

    def sum_of_divs(i):
        divs = [1]
        for d in range(2, int(sqrt(i)) + 1):
            if i % d == 0:
                divs.extend([d, i / d])
        return sum(list(set(divs)))

    for i in range(1, n):
        if sum_of_divs(i) > i:
            res.append(i)
    return res


up_bound = 28123
ab = abundants(up_bound)
ab_sum = list(set([x + y for x in ab for y in ab if (x + y) < up_bound]))

print(sum(range(up_bound)) - sum(ab_sum))
print(time.time() - tic)
