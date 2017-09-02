def sum_of_squares(n):
    return sum([x ** 2 for x in range(1, n + 1)])


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


print(square_of_sum(100) - sum_of_squares(100))
