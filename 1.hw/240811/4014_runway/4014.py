import sys
sys.stdin = open('input.txt')

def solution(data, N, X):
    for i in range(N):
        result = 0
        cnt = 0
        for j in range(N-1):
            if data[i][j] == data[i][j+1]:      # 다음 셀의 높이와 같으면 계속
                continue
            else:
                if abs(data[i][j] - data[i][j+1]) > 1:
                    break
                else:
                    temp = data[i][j]
                    cnt += 1                        # 같지 않으면 카운트 시작
                    if cnt >= X:                    # 필요 경사로의 길이가 충족되면
                        cnt = 0                     # cnt 초기화하고 계속
                        continue
                    else:                           # 카운트가 필요 경사로의 길이보다 작으면 계속





T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())                                # N: 지도의 크기, X: 경사로의 길이
    data = [list(map(int, input().split())) for _ in range(N)]      # N x N 지형의 높이

    print(f'#{tc}', result)