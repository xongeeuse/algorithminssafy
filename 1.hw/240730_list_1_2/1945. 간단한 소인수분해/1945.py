import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    prime_num = [2, 3, 5, 7, 11]

    for num in prime_num:
        counts = []
        count = 0

        while N % num == 0:
            num = N // num
            count += 1
        counts.append(count)

    a, b, c, d, e = counts



    # 틀
    # a = N // 2
    # b = N // 3
    # c = N // 5
    # d = N // 7
    # e = N // 11

    print(f'#{testcase}', a, b, c, d, e)

