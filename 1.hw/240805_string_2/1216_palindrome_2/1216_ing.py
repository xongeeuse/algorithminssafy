import sys
sys.stdin = open('input.txt')

T = 10
M = 100     # 글자판 크기 M x M

for _ in range(1, T+1):
    tc = int(input())
    data = [list(input().split()) for _ in range(M)]

    max_cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(M // 2):
            data[i][j] != data[i][M-1-j]
            break
        else:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt

    print(max_cnt)