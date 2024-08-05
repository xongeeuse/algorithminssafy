import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    ninty = []
    eighty =[]
    twentyseven = []
    for i in range(N):
        for j in range(N):
            ninty.append(arr[N-1-j][i])
            eighty.append(arr[N-1-i][N-1-j])
            twentyseven.append(arr[j][N-1-i])
    for i in range(N):
        result.append(ninty[N*i:i*N+N])
        result.append(eighty[N*i:i*N+N])
        result.append(twentyseven[N*i:i*N+N])

    C =[]
    for i in result:
        for j in range(len(i)):
            C.append(i[j])

    print(C)