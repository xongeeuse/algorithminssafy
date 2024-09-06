import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0

    for i in range(1 << N):
        '''
        부분집합의 길이와 합만 알면 되는 문제이기 때문에
        append 안 써도 됨
        '''
        length, tmp = 0, 0
        for j in range(N):
            if i & (1 << j):
                length += 1
                tmp += data[j]

                if tmp > K:
                    break

        if length == 0:
            continue
        if tmp == K:
            result += 1

    print(f'#{tc}', result)