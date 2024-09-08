import itertools
N = 4
# data = []
data = list(range(1, N + 1))
# for i in range(1, N + 1):
#     data.append(f'{i}')

print(list(itertools.combinations(data, N//2)))
# print(list(map(''.join, itertools.permutations(data))))
