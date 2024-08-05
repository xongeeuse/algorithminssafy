import sys
sys.stdin = open('input.txt')

T = 10

for testcase in range(1, T + 1):
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N):
        max1 = max(H)
        min1 = min(H)

        H[H.index(max1)] = max1 - 1
        H[H.index(min1)] = min1 + 1

        max2 = max(H)
        min2 = min(H)

        if max2 - min2 <= 1:
            break

    print(f'#{testcase}', max2 - min2)