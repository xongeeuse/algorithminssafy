import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 정수의 개수 N, 구간의 개수 M
    data = list(map(int, input().split()))
    mn, mx = float('inf'), float('-inf')

    for i in range(N - M + 1):
        tmp = 0
        for j in range(M):
            tmp += data[i + j]
        if mn > tmp : mn = tmp
        if mx < tmp : mx = tmp

    print(f'#{tc}', mx - mn)



# 딱 한 달 전 풀이
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