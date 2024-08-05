# import sys
# sys.stdin = ('input.txt')
#
# # N = int(input())
# data = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())

N = 5
data = [[1, 2, 3, 5, 10],
        [9, 7, 2, 2, 9],
        [0, 0, 1, 5, 7],
        [5, 2, 3, 2, 2],
        [1, 1, 1, 1, 1]]
K = 2


dij = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
max_kill = 0

for i in range(N):
    for j in range(N):
        kill = 0
        for di, dj in dij:
            for l in range(1, K+1):
                ni = i + di * l
                nj = j + dj * l
                if 0 <= ni < N and 0 <= nj < N:
                    kill += data[ni][nj]

        if max_kill < kill:
            max_kill = kill

print(max_kill)





# 지인 SOL
# N = 5
# arr = [[1, 2, 3, 5, 10],
#         [9, 7, 2, 2, 9],
#         [0, 0, 1, 5, 7],
#         [5, 2, 3, 2, 2],
#         [1, 1, 1, 1, 1]]
# K = 2
#
#
#
#
# di = [-1, -1, 1, 1]
# dj = [-1, 1, -1, 1]
#
# max_count = 0
#
#
# for i in range(N):
#     for j in range(N):
#         for a in range(1, K+1):
#             target = arr[i][j]  # 꼭 여기에 들어가야하는데 왜
#             for x in range(4):
#                 ni = i + (di[x] * a)
#                 nj = j + (dj[x] * a)
#                 if 0 <= ni < N and 0 <= nj < N:
#                     target += arr[ni][nj]
#                     # print(target)
#             if max_count < target:
#                 # print(max_count)
#                 max_count = target
#
# print(f'{max_count}')