import sys
sys.stdin = open('input.txt')

def solution(node):
    pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 과목의 수
    adjL = [[] for _ in range(N + 1)]               # 이수 순서 받아준 인접리스트
    adjL_reverse = [[] for _ in range(N + 1)]       # 해당 인덱스의 선수 과목 받은 인접리스트
    visited = [0] * (N + 1)
    first = []
    result = -1
    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        if data[0] == 0:
            first.append(i)
            continue
        adjL[i] = data[1:]

    if first:
        for f in first:
            solution(f)

    print(f'#{tc}', result)

    print(first)
    print(adjL)
