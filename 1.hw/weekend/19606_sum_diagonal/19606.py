import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        result += data[i][i]
        if N-i-1 != i:
            result += data[N-i-1][i]

    print(f'#{tc}', result)