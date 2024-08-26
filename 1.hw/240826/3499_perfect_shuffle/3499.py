import sys
sys.stdin = open('input.txt')

def shuffle(data):
    result = []
    if N % 2 == 0:          # 카드가 짝수 개면
        for i in range(N//2):
            result.append(data[i])
            result.append(data[(N//2) + i])

    else:                   # 카드가 홀수 개면
        for i in range(N//2):
            result.append(data[i])
            result.append(data[(N//2+1) + i])
        result.append(data[N//2])
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(input().split())
    result = shuffle(data)
    print(f'#{tc}', *result)