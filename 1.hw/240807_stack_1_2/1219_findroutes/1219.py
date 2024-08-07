import sys
sys.stdin = open('input.txt')

# 함수 수정해서 써봐~~~~~~~~~~~~~~~~~~~!
# 다시 해야 함!!!!!!!!!!!
# def DFS(s, V):              # s 시작 정점, V 정점 개수(1번부터 정점의 마지막 정점)
#     visited = [0] * (V+1)   # 방문한 정점을 표시
#     stack = []              # 스택 생성
#     print(s)
#     visited[s] = 1          # 시작정점 방문 표시
#     v = s
#     while True:
#         for w in adjL[v]:           # v에 인접하고, 방문하지 않은 w가 있으면
#             if visited[w] == 0:
#                 stack.append(v)     # push(v) 현재 정점을 push하고
#                 v = w               # w에 방문
#                 print(v)
#                 visited[w] = 1      # w에 방문 표시
#                 break               # v부터 다시 탐색
#         # for/else (break로 빠져나오지 않았으면 else문으로 이동)
#         else:                       # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
#             if stack:               # 이전 갈림길을 스택에서 꺼내서... if TOP > -1
#                 v = stack.pop()
#             else:                   # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
#                 break



T = 10

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    data = list(map(int, input().split()))
    adjL = {}
    for i in range(100):
        adjL[i] = []

    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        adjL[v1].append(v2)
        # adjL[v2].append(v1)           # 반대 방향은 필요 없음

    print(adjL)
