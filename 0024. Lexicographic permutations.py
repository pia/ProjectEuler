import itertools

x = itertools.permutations('0123456789', 10)
counter = 0
for i in x:
    counter += 1
    if counter == 1000000:
        print(''.join(i))

        # ('2', '7', '8', '3', '9', '1', '5', '4', '6', '0')
        # print(i)
    else:
        pass

# Solution 2:
# from itertools import permutations
#
# lexi_perm = list(permutations('0123456789'))
#
# solution = ''.join(lexi_perm[999999])
#
# print(solution)
