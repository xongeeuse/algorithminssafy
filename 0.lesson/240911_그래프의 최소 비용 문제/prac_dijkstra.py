'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

import heapq

INF = int(1e9)

N, M = map(int, input().split())        # N: 노드의 개수, M: 간선의 개수
start = 0                               # 시작 노드 번호
graph = [[] for _ in range(N)]          # 인접 리스트 생성
distance = [INF] * N

for _ in range(M):
    v1, v2, weight = map(int, input().split())
    graph[v1].append([v2, weight])

def dijkstra(start):
    pq = []
    # (해당 노드까지 최단 거리, 노드 번호)
    # heapq에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 가장 최단 거리 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 처리된 노드라면? (=distance 리스트에 거리 기록됨) 넘어가고!
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # 지금까지 누적된 최단 거리 + 다음 노드까지 드는 비용 계산
            new_cost = dist + cost

            # 다음 노드를 가는데 더 많은 비용이 든다면! 넘어가고!
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(start)

for i in range(N):
    if distance[i] == INF:
        print('INF', end=' ')
    else:
        print(distance[i], end=' ')