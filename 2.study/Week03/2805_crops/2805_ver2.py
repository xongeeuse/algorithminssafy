import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    result = 0
    start = N // 2
    end = N // 2 + 1

    for i in range(N):
        for j in range(start, end):
            result += data[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        elif i >= N // 2:
            start += 1
            end -= 1

    print(f'#{tc}', result)
