import sys
sys.stdin = open('input.txt')
'''
델타로 상하좌우 칸 탐색하면서 다음 칸까지의 최소비용 기록
'''
import heapq

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    distance[x][y] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if dist > distance[x][y]:               # 지금 꺼낸 dist가 이미 기록된 최단거리보다 크다면
            continue                            # 진행할 필요 없음

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:      # 범위 벗어나면 패스
                continue
            cost = data[nx][ny]         # 현재 지점에서 다음 지점으로 넘어가는 데 드는 비용

            new_cost = dist + cost      # 다음 지점으로 넘어가는데 드는 비용의 누적 값

            # '=' 안 넣었더니 무한루프 돌아버려..
            if new_cost >= distance[nx][ny]:     # 누적 값이 이미 기록된 값 이상이라면 진행할 필요 없음
                continue

            # 여기까지 넘어왔다면
            distance[nx][ny] = new_cost                 # 비용 기록해주고
            heapq.heappush(q, (new_cost, nx, ny))       # 힙에 삽입


T = int(input())
for tc in range(1, T + 1):
    N = int(input())                                            # 지도의 크기 N x N
    data = [list(map(int, list(input()))) for _ in range(N)]    # 지도 정보
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]                    # 최소 비용 저장할 리스트(초기값 INF로)

    dijkstra(0, 0)                                              # 시작점부터 다익스트라 고고
    print(f'#{tc}', distance[N - 1][N - 1])
