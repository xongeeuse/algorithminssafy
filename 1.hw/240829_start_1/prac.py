N = int(input())
result = [[0] * 7 for _ in range(2)]
# print(result)

for i in range(4):
    result[0][i] = N + i
    result[1][-1 - i] = N - i

print(result)