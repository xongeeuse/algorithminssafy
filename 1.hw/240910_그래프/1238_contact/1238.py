import sys
sys.stdin = open('input.txt')

from collections import deque

def contact(node):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        now = q.popleft()
        for v in adjL[now]:
            if not visited[v]:
                visited[v] = visited[now] + 1
                q.append(v)

T = 10
for tc in range(1, T + 1):
    N, start = map(int, input().split())
    adjL = [set() for _ in range(101)]         # 연락인원 최대 100명의 인접리스트 생성 (중복 경우 있다고 해서 set로)
    visited = [0] * 101
    data = list(map(int, input().split()))

    for i in range(0, N, 2):
        v1, v2 = data[i], data[i + 1]
        adjL[v1].add(v2)

    # print(adjL)
    contact(start)

    # 가장 마지막에 연락 받은 사람 찾기
    # 순서가 동일하다면 인덱스가 더 큰 값이 정답
    result = [0, 0]             # [0] 인덱스, [1] 연락받은 순서
    for i in range(1, 101):
        if result[1] <= visited[i]:
            result = [i, visited[i]]

    print(f'#{tc}', result[0])