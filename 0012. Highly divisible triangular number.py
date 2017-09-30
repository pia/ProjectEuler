from math import sqrt


def num_of_factors(triangle_number):
    num = 0
    if triangle_number == 1:
        return 1
    up_bound = int(sqrt(triangle_number)) + 1
    for i in range(1, up_bound):
        if triangle_number % i == 0:
            num += 1
    return (num * 2) - (1 if ((up_bound - 1) ** 2) == triangle_number else 0)


def find():
    k = 7  # kth triangle number
    while True:
        triangle_number = k * (k + 1) // 2
        if num_of_factors(triangle_number) > 500:
            return triangle_number
        k += 1


print(find())
