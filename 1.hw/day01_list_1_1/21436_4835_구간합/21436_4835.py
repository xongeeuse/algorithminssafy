import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M = (map(int, input().split()))
    arr = list(map(int, input().split()))

    maxvalue = minvalue = sum(arr[:M])

    for i in range(1, N - M + 1):
        if maxvalue < sum(arr[i : i + M]):
            maxvalue = sum(arr[i : i + M])
        if minvalue > sum(arr[i : i + M]):
            minvalue = sum(arr[i : i + M])

    result = maxvalue - minvalue

    print(f'#{testcase} {result}')