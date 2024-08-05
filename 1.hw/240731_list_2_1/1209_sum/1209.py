import sys
sys.stdin = open('input.txt')

T = 10
M = 100     # 배열의 크기 M x M

for testcase in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    max_sum = 0     # 합 중 최댓값
    sum_dgnl_1 = 0  # 대각선 값 받아줄 변수 1, 2 생성
    sum_dgnl_2 = 0

    for r in range(M):
        sum_r = 0                       # 각 행과 열의 합 받아줄 변수 1, 2 생성
        sum_c = 0                       
        sum_dgnl_1 += arr[r][r]         # 대각선의 합 1
        sum_dgnl_2 += arr[r][M-r-1]     # 대각선의 합 2

        if max_sum < sum_dgnl_1:
            max_sum = sum_dgnl_1
        if max_sum < sum_dgnl_2:
            max_sum = sum_dgnl_2

        for c in range(M):
            sum_r += arr[r][c]  # 각 행의 합
            sum_c += arr[c][r]  # 각 열의 합

        if max_sum < sum_r:
            max_sum = sum_r
        if max_sum < sum_c:
            max_sum = sum_c

    print(f'#{tc} {max_sum}')