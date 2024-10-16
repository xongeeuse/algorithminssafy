import sys
sys.stdin = open('input.txt')

T = int(input())

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 우 하 좌 상 순서


for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]     # 0으로 채워진 N x N 배열 생성

    snail[0][0] = 1
    num = 1
    x = 0
    y = 0

    while num < N ** 2:

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
                num += 1
                snail[nx][ny] = num
                x, y = nx, ny
                break
    print(f'#{tc}')

    for i in range(len(snail)):
        print(*snail[i])