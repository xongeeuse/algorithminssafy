import sys
sys.stdin = open('input.txt')

M = 100
T = 10

dxy = [[-1, 0], [0, -1], [0, 1]]    # 상, 좌, 우

def search_ladder(x, y):
    data[x][y] = 0

    while x != 0:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny]:
                data[x][y] = 0
                x, y = nx, ny

    return y


for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(M)]

    for j in range(M):
        if data[M-1][j] == 2:
            result = search_ladder(M-1, j)
            break

    print(f'#{tc} {result}')
