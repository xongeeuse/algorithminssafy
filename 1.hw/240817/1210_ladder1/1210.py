import sys
sys.stdin = open('input.txt')

def find_goal():
    for j in range(N):
        if data[N-1][j] == 2:
            return j
    return -1

def ladder(goal):
    result = -1
    visited = [[0] * N for _ in range(N)]

    x, y = N-1, goal                                # data[x][y]에서 탐색 시작
    while x != 0:
        visited[x][y] = 1                           # 방문 체크하고 시작
        for dx, dy in [[-1, 0], [0, -1], [0, 1]]:   # 상, 좌, 우 방향
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1 or data[nx][ny] == 0:
                continue
            elif nx == 0:
                result = ny
                return result
            visited[nx][ny] = 1
            x, y = nx, ny


T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]
    goal = find_goal()
    print(f'#{tc}', ladder(goal))