S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # 0~19
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]  # 0, 10~90
H = 7  # 'hundred'
T = 8  # 'thousand'
count = 0
for i in range(1, 1000):
    c = i % 10  # 个位
    b = (i % 100 - c) // 10  # 十位
    a = (i % 1000 - 10 * b - c) // 100  # 百位

    if a != 0:
        count += S[a] + H
        if b != 0 or c != 0:
            count += 3  # 'and'
    if b == 0 or b == 1:
        count += S[10 * b + c]
    else:
        count += D[b] + S[c]

count += S[1] + T  # 1000
print(count)
