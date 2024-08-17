import sys
sys.stdin = open('input.txt')

def remains(data):
    if N < M: x = M
    else: x = N

    result = 0

    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                continue
            else:
                for di, dj in [[0, 1], [1, 0]]:     # 바보.. 델타 말고 그냥 행/열로 탐색해도 되는데...
                    cnt = 1
                    for k in range(1, x):
                        ni = i + di * k
                        nj = j + dj * k
                        if ni < 0 or ni >= N or nj < 0 or nj >= M or data[ni][nj] == 0:
                            break
                        elif data[ni][nj] == 1:
                            cnt += 1
                    if result < cnt:
                        result = cnt
    # if result == 1 : return 0     # 20739_고대유적2 답변에만 추가하면 됨
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N x M 사진의 해상도
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', remains(data))