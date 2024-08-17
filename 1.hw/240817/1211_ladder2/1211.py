import sys
sys.stdin = open('input.txt')

# 시작점 찾아서 리스트로 반환하는 함수
def find_start():
    starts = []
    for j in range(N):
        if data[0][j] == 1:
            starts.append(j)
    return starts

def ladder(start):
    x, y = 0, start
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    cnt = 1
    while x != N - 1:                               # x 가 99가 아닌 동안 계속
        for dx, dy in [[1, 0], [0, -1], [0, 1]]:    # 하, 좌, 우 순서
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or not data[nx][ny] or visited[nx][ny]:
                continue                            # nx, ny가 범위 벗어나거나 길이 아니거나 이미 방문한 지점이면 패스
            elif nx == N - 1:                       # nx가 도착지점이면
                cnt += 1                            # 카운트하고
                return [start, cnt]                 # 시작점과 거리 반환

            visited[nx][ny] = 1                     # 도착 아니면 방문 위치 체크하고
            cnt += 1                                # 거리 카운트 + 1하고
            x, y = nx, ny                           # 다음 x, y 계속 진행
    # return -1



T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]
    results = []
    mn = float('inf')

    starts = find_start()
    for start in starts:
        results.append(ladder(start))

    for result in results:              # result[0] : 시작점, result[1] : 도착까지 거리
        if mn >= result[1]:
            mn = result[1]
            ans = result[0]

    print(f'#{tc}', ans)