import sys
sys.stdin = open('input.txt')

# bfs로 다시 풀어보기 계쏙 틀려어어어어

'''
수빈 N, 동생 K
수빈이가 이동하는 경우의 수 3가지
1. N - 1
2. N + 1
3. N * 2 (== N + N) / 시간 소요 X, 순간 이동

동생 위치 고정
변수는 수빈 위치, 시간

처음 생각한 접근은 dfs
다음 지점 방문 안했
'''

from collections import deque

def hide_and_seek(N, K):
    global result, cnt

    q = deque()
    visited[N] = 0
    q.append((0, N))

    while q:
        depth, now = q.popleft()
        if now == K:
            if result > depth:
                result = depth
                cnt = 1
            elif result == depth:
                cnt += 1
            continue

        if depth >= result:
            continue

        for next, time in [(now + 1, 1), (now - 1, 1), (now * 2, 0)]:
            if next < 0 or next > 100000 or visited[next] != -1:
                continue
            visited[next] = visited[now] + time
            q.append((visited[next], next))

    return cnt



N, K = map(int, input().split())
visited = [-1] * 100001

result = float('inf')
cnt = hide_and_seek(N, K)
print(cnt)
print(result)