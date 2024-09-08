import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pre_data = list(map(int, input().split()))
    data = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if pre_data[i] != data[i]:
            result += 1
            for j in range(i, N):
                pre_data[j] = 1 - pre_data[j]

    print(f'#{tc}', result)