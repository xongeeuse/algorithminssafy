import sys
sys.stdin = open('input.txt')

def bfs():
    pass

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        adjL[v1].append(v2)

    print(f'#{tc}', bfs())

