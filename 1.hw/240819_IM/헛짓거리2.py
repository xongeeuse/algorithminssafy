import sys
sys.stdin = open('input.txt')

def switch(temp, visited, num, cnt):
    global result

    while num < N+1:
        if visited[num - 1] == 0:
            visited[num - 1] = 1
            for i in range(1, N + 1):
                if i % num == 0:
                    temp[i - 1] = 1 - temp[i - 1]
            if temp == data:
                if result > cnt:
                    result = cnt
                    break
            switch(temp, visited, num+1, cnt+1)
            visited[num+1] = 0

            visited[num] = 0
            for i in range(1, N + 1):
                if i % num == 0:
                    temp[i - 1] = 1 - temp[i - 1]
            switch(temp, visited, num-1, cnt)

    return result







T = int(input())
for tc in range(1, T+1):
    N = int(input())                            # LED 등의 수
    data = list(map(int, input().split()))      # 0 : OFF, 1 : ON
    # temp = [0] * N
    # visited = [0] * N
    result = 10000000000

    print(f'#{tc}', switch(temp=[0]*N, visited=[0]*N, num=1, cnt=0))