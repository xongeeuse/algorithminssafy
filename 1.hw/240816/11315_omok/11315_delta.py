import sys
sys.stdin = open('input.txt')

dij = [[0, 1], [1, 1], [1, 0], [1, -1]] # 우, 우대각, 하, 좌대각

def is_OMOK(data):
    for i in range(N):
        for j in range(N):
            for di, dj in dij:                  # 4방향으로 탐색 예정
                cnt = 0
                if data[i][j] == 'o':           # 현 위치 'o'면 카운트 시작
                    cnt += 1
                for x in range(1, 5):           # 현 위치부터 4칸 탐색
                    ni = i + di * x
                    nj = j + dj * x

                    if 0 <= ni < N and 0 <= nj < N:     # 범위 내의 값이고
                        if data[ni][nj] == 'o':         # 'o'면 카운트
                            cnt += 1
                        else:                           # 아니면 중단
                            break
                if cnt == 5:                            # 5개 모이면 오목!
                    return 'YES'
    return 'NO'



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(N)]
    print(f'#{tc}', is_OMOK(data))