import sys
sys.stdin = open('input.txt')

def bfs(s, V): # s: 시작점, V: 마지막 정점
    # 준비
    visited = [0] * (V + 1)     # visited 생성
    q = []                      # 큐 생성
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 방문 표시
    # 탐색
    while q:
        t = q.pop(0)                # t <- 디큐
        print(t, end = ' ')         # 처리
        for w in adjL[t]:           # t에 인접이고, 인큐된 적 없으면
            if visited[w] == 0:     # 인큐하고 인큐됨 표시
                q.append(w)
                visited[w] = 1


V, E = map(int, input().split())    # V: 마지막 정점 번호, E : 간선 수
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)     # 방향이 없는 경우

bfs(1, V)   # 출발점, 정점 수
