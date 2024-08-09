import sys
sys.stdin = open('input.txt')

def escape(x, y):
    global result

    if data[x][y] == 3:
        result = 1
        return

    visited[x][y] = 1
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        # nx, ny가 범위 내의 값이면서 벽이 아니고 방문했던 지점이 아니면!
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] != 1 and visited[nx][ny] == 0:
            escape(nx, ny)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = i, j

    escape(x, y)

    print(f'#{tc}', result)