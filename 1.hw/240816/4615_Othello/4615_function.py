import sys
sys.stdin = open('input.txt')

def count_color(data):
    cnt_b = 0
    cnt_w = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                cnt_b += 1
            elif data[i][j] == 2:
                cnt_w += 1
    return cnt_b, cnt_w


def othello(x, y, stonecolor):
    global board
    i, j = y - 1, x - 1
    for di, dj in dij:
        candidates = []
        for z in range(1, N):
            ni = i + di * z
            nj = j + dj * z
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 0:              # 탐색 위치가 0이면
                    candidates = []                 # 바꾸기 후보 리스트 리셋하고 중단
                    break
                elif board[ni][nj] == stonecolor:   # 탐색 위치가 현재 놓을 돌의 색과 같으면
                    break                           # 중단
                elif board[ni][nj] != stonecolor:   # 탐색 위치가 상대편의 돌이면
                    candidates.append([ni, nj])     # 바꾸기 후보 리스트에 넣기
                    if 0 <= ni + di < N and 0 <= nj + dj < N:   # 다음 탐색 위치가 벽이 아니면
                        continue                                # 킵고잉
                    else:                                       # 벽이면
                        candidates = []                         # 후보 리스트 리셋하고 중단
                        break

        if candidates:  # 델타 방향의 돌이 나와 같은 색이고 리스트가 비어있지 않으면
            board[i][j] = stonecolor  # i, j 에 돌 놓고
            for ni, nj in candidates:
                board[ni][nj] = stonecolor  # 바꾸기 후보들 다 바꿔주기

    return






T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N: 보드의 한 변의 길이, M: 돌을 놓는 횟수
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1], board[N//2][N//2] = 2, 2             # 초기 돌 정가운데 세팅
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1

    dij = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for _ in range(M):
        x, y, stonecolor = map(int, input().split())            # stonecolor / 1 : 흑돌, 2 : 백돌
        othello(x, y, stonecolor)

    print(f'#{tc}', *count_color(board))