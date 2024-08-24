import sys
sys.stdin = open('input.txt')

# python3으로 제출하면 시간초과, pypy3으로 제출하면 통과

from collections import deque
def bfs(X):
    q = deque()
    q.append(X)
    visited[X] = 0

    while q:
        v = q.popleft()
        for k in adjL[v]:
            if visited[k] == -1:
                visited[k] = visited[v] + 1
                q.append(k)


def result(visited):
    results = []
    for i in range(len(visited)):
        if visited[i] == K:
            results.append(i)

    if not results:
        results.append(-1)

    for result in results:
        print(result)


N, M, K, X = map(int, input().split())      # N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    adjL[A].append(B)

visited = [-1] * (N + 1)
bfs(X)
result(visited)