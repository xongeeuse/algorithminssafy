import sys
sys.stdin = open('input.txt')

T = int(input())

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 우 하 좌 상 순서


for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]     # 0으로 채워진 N x N 배열 생성

    for i in range(N):
        for j in range(N):
            while not snail[i][j]:
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
