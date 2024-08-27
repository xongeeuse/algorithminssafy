import sys
sys.stdin = open('input.txt')
from collections import deque

def find_start(data):
    for i in range(M):
        for j in range(M):
            if data[i][j] == 2:
                return i, j

def miroh(i, j):
    q = deque()
    q.append([i, j])
    visited = [[0] * M for _ in range(M)]
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        if data[x][y] == 3:
            return 1
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < M and data[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
    return 0



T = 10
M = 16                  # 배열의 크기 M x M

for _ in range(T):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(M)]
    i, j = find_start(data)
    print(f'#{tc}', miroh(i, j))