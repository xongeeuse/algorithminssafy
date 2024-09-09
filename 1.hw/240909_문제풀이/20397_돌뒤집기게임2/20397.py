import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i = i - 1
        for x in range(1, j + 1):
            if i - x < 0 or i + x >= N:
                break
            if data[i - x] == data[i + x]:
                data[i - x] = 1 - data[i - x]
                data[i + x] = 1 - data[i + x]

    print(f'#{tc}', *data)