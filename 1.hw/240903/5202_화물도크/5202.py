import sys
sys.stdin = open('input.txt')

from collections import deque

'''
(작업시작시간, 종료시간) 리스트에 넣기
종료시간이 이른 작업 순으로 배열 정렬
종료시간이 이른 작업부터 시작
작업시작시간이 이전작업의 종료시간보다 크거나 같다면 다음 작업 당첨
'''

def solution(data):
    global result
    data = deque(data)

    if N == 0:
        return

    if not result:
        result += 1
        previous = data.popleft()

    while data:
        now = data.popleft()
        if previous[1] <= now[0]:
            previous = now
            result += 1




T = int(input())
for tc in range(1, T + 1):
    N = int(input())                            # N: 신청서의 개수
    data = []
    for _ in range(N):
        s, e = map(int, input().split())        # s: 작업 시작 시간, e: 종료 시간
        data.append((s, e))

    # 작업 종료 시간 기준으로 data 재정렬
    data = sorted(data, key=lambda x: x[1])

    result = 0
    solution(data)
    print(f'#{tc}', result)
