import sys
sys.stdin = open('input.txt')

def dfs(cnt, A, B):
    for i in range(N):
        if visited[i]:
            B.append(i)
            continue
        visited[i] = 1
        if cnt > N // 2:
            B.append(i)
        A.append(i)
        dfs(cnt + 1)
        visited[i] = 0




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    A, B = [], []
    visited = [0] * N
    dfs(0)
    print(A)
