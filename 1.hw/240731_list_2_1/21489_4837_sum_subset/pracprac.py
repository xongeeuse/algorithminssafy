import sys
sys.stdin = open('input.txt')

T = int(input())
arr = range(1, 13)
n = len(arr)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for i in range(1 << n):
        tmp, cnt = 0, 0
        for j in range(n):
            if i & (1 << j):
                tmp += arr[j]
                cnt += 1
        if cnt == N and tmp == K:
            result += 1

    print(f'#{tc}', result)