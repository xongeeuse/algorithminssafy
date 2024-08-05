import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]   # 특별한 의미 없는 단순 반복시 _ 사용

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0
for i in range(N):
    for j in range(N):      # N x N 배열의 모든 원소에 대해
        s = 0                # 문제에서 원소와 인접 원소의 차의 절대값의 합 저장

        # i, j 원소의 4방향 원소에 대해
        for k in range(4):
            ni = i + dj[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:         # 실존하는 인접 원소 ni, nj
                s += abs(arr[i][j] - arr[ni][nj])
        total += s      # 이 문제는 다 더하는 거라 s 없이 total에 바로 저장도 가능


print(total)