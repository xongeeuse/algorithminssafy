import sys
sys.stdin = open("input.txt")
'''
#1 61
#2 138
'''

'''
파리채 범위에 방사능 감염 파리 있다면 대각선 범위까지 터짐
+자로 터질 때와 x자로 터질 때 중복되는 부분 고려해야 함
인덱스를 받아서 중복 확인? visited 방문 체크
대각선 터질 때 또 방사능 파리 만나면 반복문 복잡해짐
재귀 써서 풀어야 하나? 다시 접근~!
'''


dij_cross = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dij_diagonal = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

def killflies_radio(x, y, visited, temp):

    for dx, dy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
        for k in range(1, M):
            nx, ny = x + dx * k, y + dy * k
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1:
                continue
            if visited[nx][ny] == 2:
                visited[nx][ny] = 1
                killflies_radio(nx, ny, visited, temp)
            else:
                visited[nx][ny] = 1
                temp += data[nx][ny]
    return temp



def killflies(data):
    global mx

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            temp = 0
            visited = visited_origin
            for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                for k in range(1, M):
                    ni, nj = i + di * k, j + dj * k
                    # ni, nj가 범위 밖이거나 이미 방문한 값이면 넘어가기
                    if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj] == 1:
                        continue
                    # ni, nj가 방사능 감염 파리면 방문 체크하고 대각선 방향 함수 진행
                    if visited[ni][nj] == 2:
                        visited[ni][nj] = 1
                        temp += killflies_radio(ni, nj, visited, temp)
                    # ni, nj가 방사능 파리도, 방문한 값도 아니라면 방문 체크하고 temp에 더하기
                    else:
                        visited[ni][nj] = 1
                        temp += data[ni][nj]

            if mx < temp:
                mx = temp

    return visited




T = int(input())
for tc in range(1, T + 1):
    N, M, B = map(int, input().split())         # N x N 배열, M x M 파리채, 방사능 감염 파리 B칸
    radio = [list(map(int, input().split())) for _ in range(B)]     # 방사능 감염 파리의 좌표
    data = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    print(data)
    visited_origin = [[0] * (N + 1) for _ in range(N + 1)]          # 인덱스 맞추기 위해 (N + 1)로 배열 생성

    for x, y in radio:                          # 방사능 파리 visited 값 2로 세팅
        visited_origin[x][y] = 2
    # print(visited_origin)

    mx = float('-inf')

    # print(N, M, B)
    # print(radio)
    # print(data)

    print(killflies(data))
    print(f'#{tc}', mx)