import sys
sys.stdin = open('input.txt')

def DFS(s, V):
    visited = [0] * (V+1)
    stack = []
    result = []
    result.append(s)
    visited[s] = 1
    v = s

    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                result.append(v)
                visited[w] = 1
                break

        else:
            if stack:
                v = stack.pop()
            else:
                break
    return map(str, result)

T = 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    adjL = [[] for _ in range(E)]

    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 +1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    print(f'#{tc}', '-'.join(DFS(1, E)))