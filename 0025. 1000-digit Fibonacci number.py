a = b = 1
index = 2
while True:
    a, b = b, a + b
    index += 1
    if b > 10 ** 999:
        print(index)
        break
