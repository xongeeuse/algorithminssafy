'''
my SOL : Python, 75,108 kb, 1,626 ms
another Python, SOL : 54,744kb, 287ms
'''


import heapq

T = int(input())
INF = int(1e9)


def dijkstar(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for test_case in range(1, T + 1):
    n, m, x = map(int, input().split())
    graph_1 = [[] for _ in range(n + 1)]
    graph_2 = [[] for _ in range(n + 1)]
    distance_1 = [INF] * (n + 1)
    distance_2 = [INF] * (n + 1)
    lst = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph_1[b].append((a, c))
        graph_2[a].append((b, c))

    dijkstar(x, graph_1, distance_1)
    dijkstar(x, graph_2, distance_2)

    for i in range(1, n + 1):
        temp = distance_1[i] + distance_2[i]
        if temp >= INF:
            temp = 0
        lst.append(temp)

    print(f'#{test_case} {max(lst)}')