import sys
sys.stdin = open('input.txt')

def switch(num):
    global temp
    for i in range(1, N+1):
        if i % num == 0:
            temp[i - 1] = 1 - temp[i - 1]

def dfs():
    global result

    for num in range(1, N+1):


T = int(input())
for tc in range(1, T+1):
    N = int(input())                            # LED 등의 수
    data = list(map(int, input().split()))      # 0 : OFF, 1 : ON
    temp = [0] * N
    result = 10000000000

    for num in range(1, N+1):
        switch(num)

    while data != temp:
        for num in range(N, 0, -1):
            switch(num)

    print(f'#{tc}', data, temp)
