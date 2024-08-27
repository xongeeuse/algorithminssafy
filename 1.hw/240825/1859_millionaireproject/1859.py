import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     print(f'#{tc}', )

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    data = list(map(int, input().split()))

    max_prices = [0] * N
    max_price = data[-1]
    for i in range(N-1, -1, -1) :
        max_price = max(max_price, data[i])
        max_prices[i] = max_price

    benefit = 0
    for i in range(N) :
        if max_prices[i] - data[i] > 0 :
            benefit += (max_prices[i] - data[i])

    print(f'#{test_case} {benefit}')