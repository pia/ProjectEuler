r = range(999, 99, -1)
is_palindome = lambda x: str(x) == str(x)[::-1]
print(max([i * j for i in r for j in r if is_palindome(i * j)]))
