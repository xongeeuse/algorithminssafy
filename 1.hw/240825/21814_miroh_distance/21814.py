import sys
sys.stdin = open('input.txt')
from collections import deque
def find_start(data):
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                return i, j

def miroh(sti, stj):
    q = deque()
    q.append([sti, stj])
    visited = [[-1] * N for _ in range(N)]
    visited[sti][stj] = 0

    while q:
        x, y = q.popleft()
        if data[x][y] == 3:
            return visited[x][y] - 1
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] != 1 and visited[nx][ny] == -1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    # 0 통로, 1 벽, 2 출발, 3 도착
    sti, stj = find_start(data)
    print(f'#{tc}', miroh(sti, stj))