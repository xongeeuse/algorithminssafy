import sys
sys.stdin = open('input.txt')

def is_possible(data):
    sold = 0

    for d in data:
        sold += 1
        total = (d // M) * K - sold         # 현재 붕어빵 재고
        if total >= 0:                      # 현재 손님에게 판매 후 재고가 0 이상이면
            continue                        # 계속
        else:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())         # N : 손님 수, M, K : 붕어빵 K마리/M초
    data = list(map(int, input().split()))

    # 도착 시간 순으로 정렬 - 선택정렬
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if data[min_idx] > data[j]:
                min_idx = j
        data[min_idx], data[i] = data[i], data[min_idx]

    print(f'#{tc}', is_possible(data))