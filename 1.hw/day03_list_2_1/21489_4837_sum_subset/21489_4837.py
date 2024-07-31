import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1, 13))
x = len(A)

for testcase in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << x):     # 부분집합의 개수만큼 반복
        subset = []
        # cnt = 0 여기 아님
        for j in range(x):      # 원소의 수만큼 비트를 비교
            if i & (1 << j):    # i의 j번 비트가 1이면
                subset.append(A[j])     # j번 원소를 subset에 넣어라
            if len(subset) == N and sum(subset) == K:
                cnt += 1

    print(f'#{testcase} {cnt}')