import sys
sys.stdin = open('input.txt')
'''
<data 정보>
.평지
* 벽돌벽(포탄 맞으면 평지)
# 강철벽
- 물
<>^v 전차방향 

전차 이동하고 나면 이전 위치 data값 평지(.)로 바꿔줘야 함!
쏘 복잡 맞나 이거
'''

dxy = {'U':[-1, 0],
       'D':[1, 0],
       'L':[0, -1],
       'R':[0, 1]}

def find_tank():
    for i in range(H):
        for j in range(W):
            if data[i][j] in '<>^v':
                return i, j

def play(x, y):
    for m in move:
        if m == 'U':
            data[x][y] = '^'
            if (x - 1) < 0:
                continue
            x -= 1
        elif m == 'D':
            data[x][y] = 'v'
            if (x + 1) >= H:
                continue
            x += 1
        elif m == 'L':
            data[x][y] = '<'
            if (y - 1) < 0:
                continue
            y -= 1
        elif m == 'R':
            data[x][y] = '<'
            if (y + 1) >= W:
                continue
            y += 1
        elif m == 'S':
            # 전차가 현재 바라보고 있는 방향으로 포탄 발사
            pass


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())       # 게임 맵 크기 H * W
    data = [list(input()) for _ in range(H)]
    N = int(input())    # 문자열 길이 N
    move = input()      # 동작
    # print(data)

    tank_x, tank_y = find_tank()
