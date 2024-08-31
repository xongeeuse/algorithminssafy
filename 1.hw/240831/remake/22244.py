import sys
sys.stdin = open('input.txt')

def find_max_len(data):
    global max_len

    for d in data:
        if max_len < len(d):
            max_len = len(d)
    return



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 배열의 길이, M: M개의 합
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, data)
    max_len = float('-inf')
    result = float('-inf')
    find_max_len(data)
    for d in data:
        if len(d) < max_len:
            d += [0] * (max_len - len(d))
    data2 = zip(data)
    print(list(data2))

    for j in range(max_len):
        temp, cnt = 0, 0

        while cnt < M:
            if cnt == M:
                if result < temp:
                    result = temp
                temp, cnt = 0, 0
                break

            for i in range(N):
                if data[i][j]:
                    temp += data[i][j]
                    cnt += 1

    print(f'#{tc}', result)


    print(data)