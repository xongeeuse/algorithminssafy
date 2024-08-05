# 지그재그 순회 연습

m = 3
n = 4

arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j + (m-1-2*j) * (i%2)])

        