import sys
sys.stdin = open('input.txt')

import heapq


# q = []
# q.pop(0)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    q = []
    for n in map(int, input().split()):
        heapq.heappush(q, n)
    print(q)