import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(N - 1):
        cnt = 0
        for j in range(i + 1, N):
            if data[i] > data[j]:
                cnt += 1
        if result < cnt:
            result = cnt

    print(f'#{tc}', result)

