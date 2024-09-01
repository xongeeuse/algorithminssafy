import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    heapq.heapify(data)
    # print(data)

    result = 0
    child = N

    while child > 1:
        parent = child // 2
        result += data[parent - 1]
        child = parent

    print(f'#{tc}', result)