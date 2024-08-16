import sys
sys.stdin = open('input.txt')

N = int(input())                                # 0 < N <= 100 : 스위치 개수
switch = list(map(int, input().split()))        # 0: OFF, 1: ON
M = int(input())                                # 0 < M <= 100 : 학생 수
data = [list(map(int, input().split())) for _ in range(M)]


for d in data:
    if d[0] == 1:                       # 남학생이면
        for i in range(N):
            if (i + 1) % d[1] == 0:     # 받은 스위치 번호의 배수인 스위치의 상태 바꾸기
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0

    elif d[0] == 2:                                     # 여학생이면
        if switch[d[1]-1] == 0 : switch[d[1]-1] = 1     # 받은 스위치 번호의 상태 바꾸고
        else: switch[d[1]-1] = 0
        start = d[1] - 1 - 1
        end = d[1]
        while 0 <= start and end < N:                   # 대칭하는 스위치 확인해서 상태 바꾸기
            if switch[start] == switch[end]:
                if switch[start] == 0 :
                    switch[start] = 1
                else:
                    switch[start] = 0
                if switch[end] == 0 :
                    switch[end] = 1
                else:
                    switch[end] = 0
                start -= 1
                end += 1
            else:                                       # 대칭이 아니면 종료
                break

# print(*switch)

for i in range(0, N, 20):
    print(*switch[i : i + 20])

