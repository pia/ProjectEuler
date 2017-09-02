def max_prime_factor(n):
    result = 0
    d = 2
    while n > 1:
        while n % d == 0:
            result = d
            n /= d
        d += 1
    return result


print(max_prime_factor(600851475143))
