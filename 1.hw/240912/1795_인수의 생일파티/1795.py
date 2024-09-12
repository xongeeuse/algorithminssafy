import sys
sys.stdin = open('input.txt')
'''
X번 집으로 오고 가는데 드는 시간 중에서 가장 오래 걸리는 집
오고 가는데!!!!!!!!!!! => 왕복 계산해줘야함!!!!!!!!!!
'''
import heapq

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next, cost in adjL[now]:
            new_cost = dist + cost
            if new_cost >= distance[next]:
                continue
            distance[next] = new_cost
            heapq.heappush(q, (new_cost, next))

    return distance


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())         # N개의 집(1 ~ N), M: 간선 개수, X: 목적지
    # adjM = [[0] * (N + 1) for _ in range(N + 1)]
    adjL = [[] for _ in range(N + 1)]
    INF = int(1e9)
    for _ in range(M):
        v1, v2, weight = map(int, input().split())
        # adjM[v1][v2] = weight
        adjL[v1].append([v2, weight])
    # print(adjL)

    to_X = [0] * (N + 1)
    for start in range(1, N + 1):
        if start == X:
            from_X = dijkstra(start)
            continue
        tmp_distance = dijkstra(start)
        to_X[start] = tmp_distance[X]


    result = 0
    for i in range(1, N + 1):
        tmp = to_X[i] + from_X[i]
        if result < tmp:
            result = tmp

    print(f'#{tc}', result)
