import sys
sys.stdin = open('input.txt', 'r')

def solution(cnt, idx, current_sum):
    global result

    if current_sum >= result:
        return

    if cnt == N - 1:
        current_sum += data[idx][0]
        if result > current_sum:
            result = current_sum
        return

    for j in range(1, N):
        if not visited[j]:
            visited[j] = 1
            solution(cnt + 1, j, current_sum + data[idx][j])
            visited[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    result = float('inf')
    for i in range(1, N):
        visited[i] = 1
        solution(1, i, data[0][i])
        visited[i] = 0

    print(f'#{tc}', result)