import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        for x in adjL[v]:
            if visited[x] == 0:
                visited[x] = visited[v] + 1
                q.append(x)
    return visited



T = 10
for tc in range(1, T + 1):
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    M = 100     # 연락 인원 최대 100명
    adjL = [[] for _ in range(M+1)]
    visited = [0] * (M+1)
    for i in range(0, N, 2):
        v1, v2 = data[i], data[i + 1]
        if v2 not in adjL[v1]:
            adjL[v1].append(v2)

    bfs(start)
    mx = 0
    result = 0
    for i in range(len(visited)):
        if mx <= visited[i]:
            mx = visited[i]
            result = i

    print(f'#{tc}', result)

