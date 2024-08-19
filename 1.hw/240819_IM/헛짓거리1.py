import sys
sys.stdin = open('input.txt')
'''
 #1 3
 #2 2
 #3 1
 #4 1
 #5 8
 '''

def switch(data, temp, num, cnt):
    global result
    # temp = [0] * N              # 모두 꺼진 스위치 상태로 초기 세팅
    # cnt = 0                     # 스위치 조작 횟수

    while 0 < num < N:              # num이 조명 개수보다 작은 동안
        for i in range(1, N+1):     # 조명 번호에 대해서
            if i % num == 0:        # 조명이 스위치의 배수라면
                temp[i - 1] = 1 - temp[i - 1]   # 상태 변경

        if temp == data:            # 상태 변경 후 원하는 결과가 만들어졌다면
            if result > cnt:        # 스위치 조작횟수 비교하고
                result = cnt        # 재할당 후
            break
        else:                       # 안 만들어졌다면
            switch(data, temp, num + 1, cnt + 1)    # 다음 스위치 계속 조작하러 가

            for i in range(1, N + 1):               # 조명 번호에 대해서
                if i % num == 0:                    # 조명이 스위치의 배수라면
                    temp[i - 1] = 1 - temp[i - 1]   # 다시 상태 변경하고
            switch(data, temp, num - 1, cnt)        # 이전으로 돌아가...아니....tlqkf..

    return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())                            # LED 등의 수
    data = list(map(int, input().split()))      # 0 : OFF, 1 : ON
    result = 1000000000000000
    temp = [0] * N
    visited = [0] * (N + 1)                     # 스위치 조작했니?

    print(f'#{tc}', switch(data, temp, num=1, cnt=0))