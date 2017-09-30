from math import sqrt

n = 2000000
p = [True] * (n + 1)
p[0], p[1] = False, False
for i in range(2, int(sqrt(n) + 1)):
    if not p[i]:
        continue
    for j in range(i * 2, n + 1, i):
        p[j] = False
primes = [x for x in range(n + 1) if p[x]]
print(sum(primes))
