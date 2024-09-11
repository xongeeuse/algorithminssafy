import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(start):
    pq = []

    # (해당 노드까지의 최단 거리, 노드 번호) 순으로 저장
    # heapq는 첫번째 요소 기준으로 정렬되니까 거리를 먼저 넣어주기
    # 시작점까지 최단 거리는 0으로 지정하고 시작
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # 현재 노드에 저장되어 있는 최단 거리가 지금 pop한 최단 거리보다 작으면 넘어가고!
        if distance[now] < dist:
            continue

        # 현재 노드의 인접 리스트에 대해 탐색 진행
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # 새로운 비용 = 현재 노드까지의 최단 거리 + 다음 노드까지 드는 비용
            new_cost = dist + cost

            # 새로운 비용이 다음 노드에 이미 기록되어 있는 최소 비용보다 크다면 넘어가고!
            if new_cost >= distance[next_node]:
                continue

            # 여기까지 넘어왔다면
            # 새로운 비용 다음 노드에 기록해주고 힙에 삽입
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))



T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())        # N: 마지막 노드 번호(0 ~ N번까지 총 노드 개수는 N + 1) E: 간선 개수
    graph = [[] for _ in range(N + 1)]      # 인접 리스트 graph[v1] = [v2, weight] 형태로 저장
    INF = int(1e9)
    distance = [INF] * (N + 1)              # 각 노드까지 최단 거리 저장할 리스트
    for _ in range(E):
        v1, v2, weight = map(int, input().split())
        graph[v1].append([v2, weight])

    start = 0
    dijkstra(start)

    print(f'#{tc}', distance[N])