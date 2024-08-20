import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = deque(map(int, input().split()))
    cnt = 0
    while cnt < M:
        tmp = data.popleft()
        data.append(tmp)
        cnt += 1
    print(f'#{tc}', data.popleft())

