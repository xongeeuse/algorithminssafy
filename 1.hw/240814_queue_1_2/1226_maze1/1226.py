import sys
sys.stdin = open('input.txt')

def find_start(data):
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                return i, j

def escape(i, j):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append([i, j])
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)
        if data[ti][tj] == 3:
            return 1
        for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and data[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return 0        # 도달 불가한 경우

T = 10
N = 16
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(data)
    print(f'#{tc}', escape(sti, stj))