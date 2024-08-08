import sys
sys.stdin = open('input.txt')

# graph: 그래프를 나타내는 인접 리스트
# start: 탐색을 시작할 정점
# visited: 방문한 정점을 저장하는 집합
# result: 탐색 경로를 저장하는 리스트
def dfs(graph, start, visited, result):
    visited.add(start)  # 현재 정점을 방문했다고 표시
    result.append(start)  # 현재 정점을 탐색 경로에 추가
    for neighbor in graph[start]:  # 현재 정점의 모든 인접 정점에 대해
        if neighbor not in visited:  # 인접 정점이 아직 방문되지 않았다면
            dfs(graph, neighbor, visited, result)  # 그 정점으로 DFS 재귀 호출



T = 10

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    data = list(map(int, input().split()))
    adjL = {}
    for i in range(100):
        adjL[i] = []

    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        adjL[v1].append(v2)
        # adjL[v2].append(v1)           # 반대 방향은 필요 없음

    # print(adjL)
    visited = set()  # 방문한 정점을 저장할 집합
    result = []  # 탐색 경로를 저장할 리스트
    dfs(adjL, 0, visited, result)
    print(result)