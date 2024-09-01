import sys
sys.stdin = open('input.txt')

def find_max_len(data):
    max_len = 0
    for d in data:
        if max_len < len(d):
            max_len = len(d)
    return max_len


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 배열의 길이, M: 구간 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    mx, mn = float('-inf'), float('inf')
    max_len = find_max_len(data)

    # 가장 긴 행의 길이만큼 0으로 채워서 길이 맞추기
    for d in data:
        if len(d) < max_len:
            d += [0] * (max_len - len(d))

    for j in range(max_len):
        for sti in range(N):
            temp, cnt = 0, 0
            for i in range(sti, N):
                if data[i][j]:
                    temp += data[i][j]
                    cnt += 1

                if cnt == M:
                    if mx < temp: mx = temp
                    if mn > temp: mn = temp
                    break

    if mx == float('-inf'):
        print(f'#{tc}', -1)
    else : print(f'#{tc}', mx - mn)