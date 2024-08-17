import sys
sys.stdin = open('input.txt')

dij1 = [[0, -1], [-1, 0], [0, 1], [1, 0]]       # + 방향 델타
dij2 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]     # x 방향 델타

def killflies(data):
    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill = data[i][j]
            kill2 = data[i][j]

            # + 형태 스프레이의 경우
            for di, dj in dij1:
                for x in range(1, M):
                    ni = i + di * x
                    nj = j + dj * x
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += data[ni][nj]
            if max_kill < kill:
                max_kill = kill

            # x 형태 스프레이의 경우
            for di, dj in dij2:
                for x in range(1, M):
                    ni = i + di * x
                    nj = j + dj * x
                    if 0 <= ni < N and 0 <= nj < N:
                        kill2 += data[ni][nj]
            if max_kill < kill2:
                max_kill = kill2

    return max_kill



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N 배열의 크기, M 스프레이 세기
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', killflies(data))