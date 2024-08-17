import sys
sys.stdin = open('input.txt')
def balloonpop(data):
    mx = 0
    mn = 10000000000
    for i in range(N):
        for j in range(N):
            tmp = - data[i][j]      # data[i][j] 값 두번 중복되는 것 보정
            for x in range(N):
                tmp += data[i][x]
                tmp += data[x][j]
            if mx < tmp : mx = tmp
            if mn > tmp : mn = tmp
    return mx - mn

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', balloonpop(data))