import sys
sys.stdin = open('input.txt')

def dfs(data):
    global answer
    if 0 not in data:
        answer = 0
        return answer

T = int(input())
for tc in range(1, T + 1):
    M, N, H = map(int, input().split())
    # 3차원 배열..?
    # 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없어요!
    data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    answer = -1
    dfs(data)
    print(f'#{tc}', answer)