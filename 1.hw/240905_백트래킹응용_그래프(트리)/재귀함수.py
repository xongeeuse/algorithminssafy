def factorial(x):
    if x == 0:
        return 1

    return x * factorial(x - 1)

print(factorial(5))

#
# def fibonacci(x):
#     # Basis Rule : n이 0일 때, 0을 반환
#     if n == 0:
#         return 0
#
#     # Basis Rule : n이 1일 때, 1을 반환
#     elif n == 1:
#         return 1
#
#     # Inductive Rule : n이 2 이상일 때, F(n - 1) + F(n - 2)을 반환
#     else:
#         return fibo(x - 1) + fibo(x - 2)


# memoization으로 피보나치 수열 구현하기
def fibonacci(x):
    if x >= 2 and memo[x] == 0:
        memo[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return memo[x]


N = 10
memo = [0] * (N + 1)                # fibonacci(n)의 결과를 n번 인덱스에 저장
memo[0] = 0
memo[1] = 1

result = fibonacci(N)