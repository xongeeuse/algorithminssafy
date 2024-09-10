import sys
sys.stdin = open('input.txt')
'''
1. 이수 순서대로 인접리스트 만들기(adjL)
2. 선수과목 기록한 인접리스트 만들기(adjL_check)
3. 선수과목이 없는 과목부터 시작해서 거리 채워가기(first리스트에 시작과목 기록)
    - first가 비어있다면 -1 리턴
4. 거리 채우기 전 확인할 사항
    - 해당 과목의 선수 과목이 모두 완료되었는가?
    - 선수 과목이 완료되었지만 같은 학기에 완료된 것은 아닌가?
        - 이 부분 인큐하는 과정에서 문제 있을 듯.. 머리 안돌아가...
5. 모든 탐색 끝났는데 아직 이수안한 과목 있으면 -1 리턴
6. 다 완료했다면 가장 큰 값이 정답
'''

from collections import deque

def check(node, now):
    for v in adjL_check[node]:                                          # 해당 과목의 선수과목 리스트에서
        if not visited[v] or visited[v] == visited[now] + 1:            # 완료하지 않은 과목이 있거나 해당 학기에 완료했다면 False 반환
            return False
    return True                                                         # 다 완료했다면 True 반환


def solution(node):
    global result
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        now = q.popleft()
        for v in adjL[now]:
            if not visited[v]:
                if check(v, now):
                    visited[v] = visited[now] + 1
                    q.append(v)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N: 과목의 수
    adjL = [[] for _ in range(N + 1)]           # 해당 인덱스 이후 이수할 수 있는 과목 기록된 인접 리스트
    adjL_check = [[] for _ in range(N + 1)]     # 해당 인덱스의 선수 과목 기록된 인접 리스트 (reverse)
    visited = [0] * (N + 1)
    first = []                                  # 선수 과목 없는 시작점 후보
    result = -1

    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        if data[0] == 0:                        # 선수 과목 없다면 시작점 후보에 넣고
            first.append(i)
            continue
        adjL_check[i] = data[1:]                # 있다면 해당 인덱스의 선수 과목 기록하고
        for v in data[1:]:                      # 이후 이수할 수 있는 과목도 기록하기
            adjL[v].append(i)

    if first:                           # 모든 시작점에 대해 탐색 시작
        for f in first:
            solution(f)

    if 0 not in visited[1:]:            # 모든 과목 이수했다면(0번 인덱스 제외)
        result = max(visited)           # 가장 큰 값이 최소 이수해야 할 학기 수

    print(f'#{tc}', result)