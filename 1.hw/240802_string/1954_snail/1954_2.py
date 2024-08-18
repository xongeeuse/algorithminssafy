import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [[0] * N for _ in range(N)]
    x, y = 0, 0
    num = 1
    result[x][y] = num

    while num < N ** 2:
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and result[nx][ny] == 0:
                num += 1
                result[nx][ny] = num
                x, y = nx, ny
                break

    print(f'#{tc}')
    for r in result:
        print(*r)