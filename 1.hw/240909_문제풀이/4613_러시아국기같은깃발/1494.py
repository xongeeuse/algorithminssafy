import sys
sys.stdin = open('input.txt')
'''
흰
파
빨
'''
def make_flags(data):
    mn = N * M

    cnt_w = 0
    for i in range(N - 2):
        for j in range(M):
            if data[i][j] != 'W':
                cnt_w += 1

        cnt_b = 0
        for k in range(i + 1, N - 1):
            for j in range(M):
                if data[k][j] != 'B':
                    cnt_b += 1

            cnt_r = 0
            for l in range(k + 1, N):
                for j in range(M):
                    if data[l][j] != 'R':
                        cnt_r += 1

            if mn > cnt_w + cnt_b + cnt_r:
                mn = cnt_w + cnt_b + cnt_r

    return mn


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    print(f'#{tc}', make_flags(data))