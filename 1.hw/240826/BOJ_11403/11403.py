import sys
sys.stdin = open('input.txt')

def dfs():

    for i in range(N):
        for j in range(N):
            if adjM[i][j] == 1 and visited[i][j] == 0 :

  pass

T = int(input())
for tc in range(1, T + 1):
    N = int(input())                                            # N 정점의 개수
    adjM = [list(map(int, input().split())) for _ in range(N)]  # 인접 행렬
    result = [[0] * N for _ in range(N)]

    # print(adjM)

    print(f'#{tc}')
    for i in range(N):
        print(*result[i])

    # print(*result)
