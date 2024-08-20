import sys
sys.stdin = open('input.txt')

def bfs(start, goal):
    q = [start]                         # q에 시작점 넣고
    visited[start] = 1                  # 방문 체크

    while q:                            # q가 있는 동안
        v = q.pop(0)                    # q의 첫 요소인 v에 대해서
        for x in adjL[v]:               # v의 인접리스트를 탐색할거야
            if visited[x] == 0:         # x를 방문한 적 없으면
                visited[x] = visited[v] + 1     # 이전 거리에서 하나 더한 값을 주고
                q.append(x)                     # q에 다음 탐색후보로 넣기
            if x == goal:                       # 만약 x가 도착점이라면
                return visited[x] - 1           # 거리에서 -1한 값을 리턴하세요

    return 0





T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    start, goal = map(int, input().split())
    visited = [0] * (V + 1)

    print(f'#{tc}', bfs(start, goal))