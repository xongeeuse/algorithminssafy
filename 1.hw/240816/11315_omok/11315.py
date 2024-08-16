import sys
sys.stdin = open('input.txt')
'''
00 01 02 03 04 05
10 11 12 13 14 15
20 21 22 23 24 25
30 31 32 33 34 35
40 41 42 43 44 45
50 51 52 53 54 55
'''

def is_OMOK(data):

    for i in range(N):
        cnt_r = 0
        cnt_c = 0
        for j in range(N):
            # 가로 방향 확인
            if data[i][j] == 'o':
                cnt_r += 1
                if cnt_r == 5:
                    return 'YES'
            else:
                cnt_r = 0

            # 세로 방향 확인
            if data[j][i] == 'o':
                cnt_c += 1
                if cnt_c == 5:
                    return 'YES'
            else:
                cnt_c = 0

    # 대각선 확인 1
    x = 0
    cnt_d = 0
    for i in range(N):
        for j in range(N):
            while 0 <= i + x < N and 0 <= j + x < N and data[i + x][j + x] == 'o':
                cnt_d += 1
                x += 1

                if cnt_d == 5:
                    return 'YES'

                if i + x >= N or j + x >= N:
                    break

    # 대각선 확인 2
    x = 0
    cnt_d = 0
    for i in range(N):
        for j in range(N):
            while 0 <= i + x < N and 0 <= j - x < N and data[i + x][j - x] == 'o':
                cnt_d += 1
                x += 1

                if cnt_d == 5:
                    return 'YES'

                if i + x >= N or j - x < 0:
                    break

    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(N)]
    print(f'#{tc}', is_OMOK(data))
