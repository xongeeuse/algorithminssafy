import sys
sys.stdin = open('input.txt')

dxy = [[0, 1], [1, 0]]  # 우, 하
# def solution(data, x, y, tmp):
#     global mn
#     for dx, dy in dxy:
#         nx, ny = x + dx, y + dy
#         if nx == (N - 1) and ny == (N - 1):
#             if mn > tmp: mn = tmp
#         if nx < 0 or nx >= N or ny < 0 or ny >= N:
#             break
#         if data[nx][ny]:
#             solution(data, nx, ny, tmp + data[x][y])

def find_min_route(data, x, y, current_sum):
    global mn

    for dx, dy in [[0, 1], [1, 0]]:  # 우, 하
        nx, ny = x + dx, y + dy

        # 백트래킹 가지치기
        if current_sum >= mn:                           # 현재까지의 합이 이미 mn 이상이면 중단
            break

        if nx < 0 or nx >= N or ny < 0 or ny >= N:      # nx, ny가 범위를 넘어가면 continue
            continue
        if nx == (N - 1) and ny == (N - 1):             # nx, ny가 도착점이면
            current_sum += data[nx][ny]                 # current_sum에 도착점의 값 더해주고
            if mn > current_sum:                        # 기존 mn과 비교해서 재할당
                mn = current_sum
            return
        find_min_route(data, nx, ny, current_sum + data[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    mn = 10000
    find_min_route(data, 0, 0, current_sum=data[0][0])
    print(f'#{tc}', mn)
