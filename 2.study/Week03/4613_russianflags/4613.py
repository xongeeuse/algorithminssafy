import sys
sys.stdin = open('input.txt')

def make_flags(data):

    cnt = 0
    for j in range(M):
        if data[0][j] != 'W':
            data[0][j] = 'W'
            cnt += 1
        if data[N-1][j] != 'R':
            data[N-1][j] = 'R'
            cnt += 1
    return cnt



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    print(f'#{tc}', make_flags(data))