import sys
sys.stdin = open('input.txt')

T = 10
M = 100

for testcase in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    di = [0, 1, 0]
    dj = [1, 0, -1]

    for i in range(M):
        for j in range(N):
            for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[ni][nj] == 1:



