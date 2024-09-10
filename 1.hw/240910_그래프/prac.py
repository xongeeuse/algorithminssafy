'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(node):
    print(node, end=' ')

    for v in adjL[node]:
        if not visited[v]:
            visited[node] = 1
            dfs(v)





data = list(map(int, input().split()))
N = len(data)
M = 7
adjL = [[] for _ in range(M + 1)]
visited = [0] * (M + 1)

for i in range(0, N, 2):
    v1, v2 = data[i], data[i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)
# print(adjL)

start = 1
visited[start] = 1
dfs(start)