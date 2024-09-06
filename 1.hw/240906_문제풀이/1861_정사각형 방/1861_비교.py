import sys
sys.stdin = open('input.txt', "r")

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))


def dfs():
    for i in range(N):
        for j in range(N):
            for dr, dc in dir:
                nr = i + dr
                nc = j + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if arr[nr][nc] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    break

    cnt = max_cnt = start = 0
    for i in range(N ** 2, -1, -1):     # 방 번호 끝부터 탐색
        if visited[i]:                  # i번 방 방문한 적 있으면
            cnt += 1                    # 이동횟수 + 1
        else:
            if max_cnt <= cnt:          # 최대 이동횟수
                max_cnt = cnt
                start = i + 1
            cnt = 0
    return start, max_cnt


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    start, max_cnt = dfs()
    print(f"#{t} {start} {max_cnt + 1}")