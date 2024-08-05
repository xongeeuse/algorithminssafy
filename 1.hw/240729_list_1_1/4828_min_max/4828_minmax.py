import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max = arr[0]
    min = arr[0]

    for i in range(1, N):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]

    print(f'#{testcase}', max - min)

