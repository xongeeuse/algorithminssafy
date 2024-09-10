import sys
sys.stdin = open('input.txt')

'''
사용할 수 있는 연산
+1, -1, *2, -10
'''

# def dfs(cnt, current_num):
#     global result
#
#     # 기저조건: 연산 결과가 M이면 연산횟수 반환하고 종료
#     if current_num == M:
#         result = min(result, cnt)
#         return
#
#     # 연산의 중간 결과도 항상 백만 이하의 자연수
#     if current_num > 1000000:
#         return
#
#     dfs(cnt + 1, current_num + 1)
#     dfs(cnt + 1, current_num - 1)
#     dfs(cnt + 1, current_num * 1)
#     dfs(cnt + 1, current_num - 10)

from collections import deque

def bfs(N, cnt):
    global result
    q = deque()
    visited[N] = 1
    q.append((N, cnt))

    # while q:
    #     num = q.popleft()
    #     if num == M:
    #         break
    #     if num > 1000000:
    #         continue
    #
    #     if visited[num] == -1:
    #         for i in [num + 1, num - 1, num * 2, num - 10]:
    #             visited[i] = visited[num] + 1
    #             q.append(i)

    while q:
        num, cnt = q.popleft()
        if num == M:
            result = cnt
            break
        if num > 1000000:
            continue

        for i in [num + 1, num - 1, num * 2, num - 10]:
            if 0 <= i < 1000001 and visited[i] == 0:
                visited[i] = 1
                q.append((i, cnt + 1))



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # 자연수 N에 몇 번의 연산을 통해 자연수 M 만들기
    visited = [0] * 1000001
    result = 0
    bfs(N, 0)
    print(f'#{tc}', result)