import sys
sys.stdin = open('input.txt')

def dfs(intersection, visited):
    global result

    if result == 1:             # 결과가 1이면 탐색 종료
        return

    if intersection == end:     # 현재 시작지점이 도착지점과 같으면
        result = 1              # 결과 1
        return

    visited[intersection] = True    # 현 위치 방문 표시

    for adj in adjL[intersection]:  # 현 위치의 인접리스트를 순회하면서
        if visited[adj] == True:    # 이미 방문한 지점이면 패스하고
            continue
        dfs(adj, visited)           # 새로운 지점일 경우 탐색 재진행




T = 10

for _ in range(1, T+1):
    tc, N = map(int, input().split())
    data = list(map(int, input().split()))
    size, start, end = 100, 0, 99
    result = 0

    adjL = {}
    for i in range(100):
        adjL[i] = []

    for i in range(N):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        adjL[v1].append(v2)
        # adjL[v2].append(v1)           # 반대 방향은 필요 없음

    visited = [False] * size
    dfs(start, visited)

    print(f'#{tc}', result)