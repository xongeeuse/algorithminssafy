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
    max_len = float('-inf')
    result = float('-inf')
    find_max_len(data)

    for d in data:
        if len(d) < max_len:
            d += [0] * (max_len - len(d))

    organized = list(map(list, zip(*data)))

    for i in range(N - M + 1):
        temp, cnt = 0, 0






    print(data)
    print(organized)