import sys
sys.stdin = open('sample_input.txt')
"""
8
14
9
"""
def backtrack(x, y, visited_row, visited_col, depth, current_sum):
    global min_sum

    # current_sum += data[x][y]               # 부분집합 원소 합에 더하기

    if current_sum >= min_sum:              # 현재 부분집합의 합이 최솟값 이상이면
        return                              # 더 깊이 탐색할 필요 없음

    if depth == N:                          # 모든 수에 대해 확인 했다면 최솟값과 비교 후 반환
        if min_sum > current_sum:
            min_sum = current_sum
        return

    for i in range(N):
        for j in range(N):
            if visited_row[i] == 0 and visited_col[j] == 0:     # 행, 열 모두 방문한 적 없으면
                x, y = i, j# 다음 행선지 낙찰
                visited_row[x], visited_col[y] = 1, 1  # 현재 탐색 지점의 행, 열 방문 체크하고
                backtrack(x, y, visited_row, visited_col, depth + 1, current_sum + data[x][y])
                visited_row[x], visited_col[y] = 0, 0  # 현재 탐색 지점의 행, 열 방문 체크하고

    # backtrack(x, y, visited_row, visited_col, depth + 1, current_sum)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000   # 최소 합
    # visited_row = [0] * N   # 행 방문체크 리스트
    # visited_col = [0] * N   # 열 방문체크 리스트

    # for j in range(N):
    backtrack(0, 0, visited_row=[0]*N, visited_col=[0]*N, depth=0, current_sum=0)

    print(f'#{tc}', min_sum)
