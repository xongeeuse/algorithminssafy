import sys
sys.stdin = open('input.txt')

##### my SOL
def millionaire(data):
    result = 0
    best_prices = [0] * N           # 최고가 저장할 리스트 생성
    best = data[-1]                 # 마지막날의 예측가를 초기 최고가로 설정
    for i in range(N-1, -1, -1):
        if best < data[i]:
            best = data[i]
        best_prices[i] = best

    for i in range(N):
        if data[i] < best_prices[i]:                # 현재 가격이 이후 최고가보다 작을 때만
            result += (best_prices[i] - data[i])    # 구매하고 차액을 결과에 더하기

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc}', millionaire(data))


# ##### 모르겠어서 찾아봄
# ##### SOL

# T = int(input())
# for test_case in range(1, T+1) :
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     max_prices = [0] * N
#     max_price = data[-1]
#     for i in range(N-1, -1, -1) :
#         max_price = max(max_price, data[i])
#         max_prices[i] = max_price
#
#     benefit = 0
#     for i in range(N) :
#         if max_prices[i] - data[i] > 0 :
#             benefit += (max_prices[i] - data[i])
#
#     print(f'#{test_case} {benefit}')