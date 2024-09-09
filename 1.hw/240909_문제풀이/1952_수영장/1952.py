import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    day, month, quarter, year = map(int, input().split())
    data = [0] + list(map(int, input().split()))        # 인덱스 맞춰주기
    dp = [0] * 13

    for i in range(1, 13):
        # 일간, 월간 이용권 중 적은 금액 넣어주기
        dp[i] = dp[i - 1] + min(data[i] * day, month)

        if i >= 3:
            # 3월부터는 이전 달 최소금액 + (일간 vs 월간) vs 3개월 이전 최소금액 + 3개월 이용권 금액 비교
            dp[i] = min(dp[i - 1] + data[i] * day, dp[i - 1] + month, dp[i - 3] + quarter)

    # 최소비용 계산 끝난 후에는
    # 12월 까지의 최종 최소비용 vs 연간 이용권 금액 비교
    result = min(dp[12], year)


    print(f'#{tc}', result)
