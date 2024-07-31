import sys
sys.stdin = open('input.txt')

T = 10

for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    goodview = []
    result = 0

    for i in range(2, N-2):

        l_temp = 0
        r_temp = 0

        # 좌측 둘 비교
        if arr[i - 1] > arr[i - 2]:
            l_temp = arr[i - 1]
        else:
            l_temp = arr[i - 2]

        # 우측 둘 비교
        if arr[i + 1] > arr[i + 2]:
            r_temp = arr[i + 1]
        else:
            r_temp = arr[i + 2]

        # 
        if r_temp > l_temp:
            goodview.append(arr[i] - r_temp)
        else:
            goodview.append(arr[i] - l_temp)

    # 양수만 더하기
    for item in goodview:
        if item > 0:
            result += item

    print(f'#{testcase} {result}')