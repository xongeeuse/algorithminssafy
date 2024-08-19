import sys
sys.stdin = open('input.txt')

'''
#1 3
#2 2
#3 1
#4 1
#5 8
'''

# 하......

T = int(input())
for tc in range(1, T+1):
    N = int(input())                            # LED 등의 수
    data = list(map(int, input().split()))      # 0 : OFF, 1 : ON
    temp = [0] * N
    result = 0

    for i in range(1, N + 1):
        if data[i - 1] == 1 and temp[i - 1] == 0:
            result += 1
            for j in range(N):
                if (j + 1) % i == 0:
                    temp[j] = 1 - temp[j]

        elif data[i - 1] == 0 and temp[i - 1] == 1:
            result += 1
            for j in range(N):
                if (j + 1) % i == 0:
                    temp[j] = 1 - temp[j]

    print(f'#{tc}', result)
