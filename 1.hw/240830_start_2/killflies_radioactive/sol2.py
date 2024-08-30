import sys
sys.stdin = open("input.txt")

def kill_Bfly(k,l):
    # global k, l, i, j
    fly = 0
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
    for a in range(4):
        # for b in range(1, M):
        nr = k + dr[a]
        nc = l + dc[a]
        if 0 <= nr < N and 0 <= nc < N:
            if [nr + 1, nc + 1] in Bfly:
                fly += kill_Bfly(nr, nc)

            if not visited[nr][nc]:
                visited[nr][nc] = 1
                fly += arr[nr][nc]



    return fly

T = int(input())
for tc in range(1, T+1):
    N, M, B = map(int, input().split())
    Bfly = [list(map(int, input().split())) for _ in range(B)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(Bfly)
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            visited = [[0]*N for _ in range(N)]
            fly = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    if not visited[k][l]:
                        fly += arr[k][l]
                        visited[k][l] = 1
                    if [k+1,l+1] in Bfly:
                        fly += kill_Bfly(k,l)

            if result < fly:
                result = fly
    print(f'#{tc} {result}')