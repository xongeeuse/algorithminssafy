import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    n = len(arr)
    sum_tmp = 0

    for i in range(1 << n):
        subset = []
        sum_tmp = 0
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
                sum_tmp += arr[j]
        if len(subset) >= 1 and sum_tmp == 0:
            result = 1
            break
    print(f'#{testcase}', result)



