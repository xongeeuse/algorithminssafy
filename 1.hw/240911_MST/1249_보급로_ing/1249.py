import sys
sys.stdin = open('input.txt')

import heapq


def dijkstra(x, y):
    pq = []
    # (해당 노드까지의 최단 거리, x, y)
    heapq.heappush(pq, (0, x, y))
    distance[x][y] = 0

    while pq:
        # 가장 최단 거리 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(pq)

        # 이미 기록되어 있는 거리가 현재 꺼낸 거리보다 작다면 넘어가고!
        if distance[x][y] < dist:
            continue

        # 현재 노드의 인접노드 확인할게요~
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            # 범위 벗어나면 넘어갑니다~
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 다음 노드까지 드는 비용 변수에 기록할건데 기본 비용은 1
            cost = 1
            # 다음 노드의 높이가 현재 노드보다 높다면
            # 높이의 차이만큼 비용에 더하기
            if data[x][y] < data[nx][ny]:
                cost += (data[nx][ny] - data[x][y])

            # 지금까지의 거리에 누적한 비용 변수에 기록
            new_cost = dist + cost
            # 누적 비용이 이미 기록된 최단 거리 이상이라면 넘어갈게요~
            if new_cost >= distance[nx][ny]:
                continue

            # 여기까지 넘어왔다면 비용 기록해주고 힙에 삽입
            distance[nx][ny] = new_cost
            heapq.heappush(pq, (new_cost, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split()))]
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc}', )
