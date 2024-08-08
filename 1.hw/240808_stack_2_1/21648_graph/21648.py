import sys
sys.stdin = open('input.txt')

def dfs(S):
    global result

    if S == G:
        result = 1
        return

    visited[S] = 1

    for adj in adjL[S]:
        if visited[adj] == 1:
            continue
        dfs(adj)





T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = {}                               # 인접 리스트 틀 생성
    for i in range(1, V+1):
        adjL[i] = []

    for _ in range(E):                      # 간선 정보 인접 리스트에 담기
        x, y = map(int, input().split())
        adjL[x].append(y)

    S, G = map(int, input().split())        # S: 출발점, G: 도착점
    visited = [0] * (V + 1)
    result = 0

    dfs(S)

    print(f'#{tc}', result)