import sys
sys.stdin = open('input.txt')

def search_guard():
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                return i, j

def safe_area(i, j):
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        for k in range(1, N):
            ni, nj = i + di * k, j + dj * k
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            if data[ni][nj] == 1:
                break
            visited[ni][nj] = 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 지도 한 변의 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    i, j = search_guard()
    safe_area(i, j)
    result = 0

    for i in range(N):
        for j in range(N):
            if not data[i][j] and not visited[i][j]:
                result += 1

    print(f'#{tc}', result)