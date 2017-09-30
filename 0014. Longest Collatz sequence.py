def next(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2


class ChainCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(next(n))  # 递归
            self.cache[n] = c + 1
            return c + 1


length = ChainCache()


def max_len(x):
    v, m = 0, 0
    for i in range(1, x):
        l = length(i)
        if l > m:
            v, m = i, l
    return v


print(max_len(1000000))
