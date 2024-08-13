import sys
sys.stdin = open('input.txt')

# 인덱스 갈아주기 ver.
# def password_generator(data):
#     while 1:
#         for num in range(1, 6):
#             result = data[0] - num
#             for i in range(N - 1):
#                 data[i] = data[i + 1]
#             data[N - 1] = result
#             if data[N - 1] <= 0:
#                 data[N - 1] = 0
#                 return data

# pop/append ver.
def password_generator(data):
    while True:
        for num in range(1, 6):
            if data[0] - num > 0:
                data.append(data[0] - num)
                data.pop(0)
            else:
                data.append(0)
                data.pop(0)
                return data
    # return data


T = 10

for _ in range(1, T + 1):
    tc = int(input())
    data = list(map(int, input().split()))
    N = 8

    print(f'#{tc}', *password_generator(data))