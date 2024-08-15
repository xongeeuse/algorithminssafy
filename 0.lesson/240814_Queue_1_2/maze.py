def bfs(i, j, N):
    visited = [[0] * N for i in range(N)]
    q = []
    q.append([i, j])
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 1 - 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0        # 도달 못하는 경우


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc}', ans)