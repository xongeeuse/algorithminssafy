import sys
sys.stdin = open('input.txt')

'''
사용할 수 있는 연산
+1, -1, *2, -10
'''

# 완탐인데 런타임에러남
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

def bfs(N):
    # global result
    q = deque()
    q.append(N)
    
    # visited에 거리를 바로 저장하는 방법
    while q:
        num = q.popleft()
        if num == M:
            break

        for i in [num + 1, num - 1, num * 2, num - 10]:
            if 0 < i <= 1000000 and visited[i] == -1:          # i 범위 조건 넣어야 런타임에러 안나고 통과
                visited[i] = visited[num] + 1
                q.append(i)
    
    # q에 (num, cnt) 형태로 인큐하면서 진행하는 방법
    # while q:
    #     num, cnt = q.popleft()
    #     if num == M:
    #         result = cnt
    #         break
    #     if num > 1000000:
    #         continue
    #
    #     for i in [num + 1, num - 1, num * 2, num - 10]:
    #         if 0 < i <= 1000000 and visited[i] == 0:
    #             visited[i] = 1
    #             q.append((i, cnt + 1))



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # 자연수 N에 몇 번의 연산을 통해 자연수 M 만들기
    visited = [-1] * 1000001
    # result = 0
    visited[N] = 0
    bfs(N)
    print(f'#{tc}', visited[M])