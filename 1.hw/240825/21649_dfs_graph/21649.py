import sys
sys.stdin = open('input.txt')

def dfs(start):
    if start not in visited:
        visited.append(start)

    for v in adjL[start]:
        if v not in visited:
            dfs(v)

    return map(str, visited)



T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V 정점의 개수, E 간선의 개수
    data = list(map(int, input().split()))
    adjL = [[] for _ in range(V + 1)]
    visited = []
    for i in range(0, E):
        v1, v2 = data[i * 2], data[(i * 2) + 1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visited = dfs(1)
    print('-'.join(visited))


