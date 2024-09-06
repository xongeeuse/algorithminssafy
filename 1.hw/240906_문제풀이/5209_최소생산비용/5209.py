import sys
sys.stdin = open('input.txt')

def solution(row, current_sum):
    global mn
    if current_sum >= mn:
        return

    if row == N:
        if mn > current_sum:
            mn = current_sum
        return

    for col in range(N):
        if visited[col]:
            continue

        visited[col] = 1
        solution(row + 1, current_sum + data[row][col])
        visited[col] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    mn = float('inf')

    solution(row= 0, current_sum= 0)
    print(f'#{tc}', mn)
