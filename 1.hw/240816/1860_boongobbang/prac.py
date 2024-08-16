'''
2
4 30 10
10 20 30 40
6 5 1
10 20 25 14 10
'''

def is_possible(data):
    sold = 0
    for d in data:
        stock = d // M * K - sold       # 현재 붕어빵 재고
        if stock > 0:                   # 한마리 이상이면
            sold += 1                   # 카운트하고
                                        # 계속
        else:
            return 'Impossible'
    return 'Possible'

N, M, K = 4, 10, 10
data = [10, 20, 30, 40]
print(is_possible(data))

# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())         # N : 손님 수, M, K : 붕어빵 K마리/M초
#     data = list(map(int, input().split()))
#
#     # 도착 시간 순으로 정렬 - 선택정렬
#     for i in range(N-2):
#         min_idx = i
#         for j in range(i + 1, N-1):
#             if data[min_idx] > data[j]:
#                 min_idx = j
#         data[min_idx], data[i] = data[i], data[min_idx]
#
#     print(f'#{tc}', is_possible(data))
