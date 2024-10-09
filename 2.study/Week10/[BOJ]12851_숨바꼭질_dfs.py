import sys
sys.stdin = open('input.txt')
'''
수빈 N, 동생 K
수빈이가 이동하는 경우의 수 3가지
1. N - 1
2. N + 1
3. N * 2 (== N + N)

동생 위치 고정
변수는 수빈 위치, 시간
'''

# DFS
# 런타임 에러 (RecursionError)에서 아래 추가하면
# import sys
# sys.setrecursionlimit(100000)
# 시간초과..


def hide_and_seek(depth, now):
    global result

    if now == K:
        if result > depth:
            result = depth
        return

    if depth >= result:
        return

    for next, time in [[now - 1, 1], [now + 1, 1], [now * 2, 0]]:
        if next < 0 or next > 100000 or visited[next]:
            continue
        visited[next] = 1
        hide_and_seek(depth + time, next)
        visited[next] = 0


N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
visited[N] = 1

result = float('inf')
hide_and_seek(0, N)
print(result)