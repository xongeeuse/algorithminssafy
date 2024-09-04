# another SOL 1
# 나랑 비슷한 거
# from collections import deque
#
# # 모든 물을 출발점으로 하는 BFS를 돌리자
# def bfs(N, M):
#     ans = 0  # 최단 거리의 합
#     q = deque()  # 큐 생성
#     visited = [[-1] * M for _ in range(N)]  # visited 생성
#     for i in range(N):  # 출발점(모든 물) 인덱스 인큐
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 q.append((i, j))  # 출발점 인큐 표시
#                 visited[i][j] = 0
#
#     while q:  # 탐색할 땅이 남아 있으면
#         i, j = q.popleft()  # 인접한 땅을 조사할 격자칸 인덱스 디큐
#         for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#                 ans += visited[ni][nj]
#     return ans
#     # 출발점 인큐 표시
#
#
# for t in range(1, int(input()) + 1):
#     N, M = map(int, input().split())  # N x M 크기의 격자
#     arr = [input() for _ in range(N)]
#
#     ans = bfs(N, M)  # 모든 땅에서 물까지의 최단 거리
#     print(f'#{t} {ans}')



# 2
# 메모리, 시간 적게 드는 버전
from collections import deque


def BFS():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        now = queue.popleft()

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[now[0]][now[1]] + 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    queue = deque()
    visited = [[-1] * M for _ in range(N)]
    # 물인지 아닌지 찾기 전에는 -1
    # 물이면 0
    # 나중에 땅에서 물까지의 거리를 계산할 때에는 물에서부터의 거리를 넣어준다

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W' and visited[r][c] == -1:
                queue.append((r, c))
                visited[r][c] = 0

    BFS()

    result = 0
    for r in range(N):
        for c in range(M):
            result += visited[r][c]

    print(f'#{tc} {result}')