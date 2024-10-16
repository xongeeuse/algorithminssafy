import sys
sys.stdin = open('input.txt')
'''
시간초가ㅗ~
1. 원래 접근
모든 땅을 찾아서 출발지 리스트에 넣고 하나씩 돌면서 물까지의 거리 카운트

2. 수정
물의 좌표만 찾아서 방문하지 않은 땅이 나올 때 마다 거리 더해주기
- 물이 하나가 아닌 경우 고려?
- 이미 지나간 경론데 다음 물에서 출발했을 때 더 최소경로라면 업데이트
    - 아니 bfs라서 안해도 돼 걍 물부터 출발할거라
'''


from collections import deque

def go_to_water(data):
    global result

    for i in range(N):
        for j in range(M):
            if data[i][j] == 'W':       # 물이면
                visited[i][j] = 0       # 0으로 방문 처리하고
                q.append((i, j))        # 인큐

    while q:
        x, y = q.popleft()

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy

            # or 때문에 시간이 오래걸리나 해서 아래 방식으로 변경
            # if nx < 0 or nx >= N or ny < 0 or ny >= M:          # 범위 초과면 패스
            #     continue
            # if visited[nx][ny] != -1:                           # 방문한 적 있으면 패스
            #     continue
            #
            # visited[nx][ny] = visited[x][y] + 1
            # result += visited[nx][ny]
            # q.append((nx, ny))


            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1                     # 범위 내의 값이고 방문한 적 없으면 방문체크하고
                result += visited[nx][ny]                               # 결과에 현재 거리 더해주고
                q.append((nx, ny))                                      # 인큐



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    q = deque()                                 # 탐색 후보 덱으로 받을 예정
    visited = [[-1] * M for _ in range(N)]      # visited -1로 기본 세팅
    result = 0                                  # 땅까지의 거리 받아줄 변수 생성

    go_to_water(data)

    print(f'#{tc}', result)