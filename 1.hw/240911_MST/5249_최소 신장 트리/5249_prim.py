import sys
sys.stdin = open('input.txt')

import heapq

# prim 방식으로
def make_MST(start):
    # 가중치가 가장 낮은 값을 우선 탐색 대상으로 활용(최소힙)
    q = []
    visited = [0] * (V + 1)
    temp_sum = 0

    # (가중치, 정점 정보) : 시작 노드니까 가중치 0으로 시작
    # 최소힙 구성의 비교 대상이 가중치이므로, 가중치부터 삽입
    heapq.heappush(q, (0, start))

    while q:
        weight, now = heapq.heappop(q)
        if not visited[now]:
            visited[now] = 1
            temp_sum += weight
            for next in range(V + 1):
                # 간선이 존재하고 방문한 적 없다면!
                if graph[now][next] and not visited[next]:
                    # 힙에 값 푸시
                    heapq.heappush(q, (graph[now][next], next))

    return temp_sum


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())     # V: 마지막 노드 번호(0 ~ V번), E: 간선 개수
    graph = [[0] * (V + 1) for _ in range(V + 1)]   # 가중치 인접 행렬 형태로 저장
    # result = float('inf')
    for _ in range(E):
        v1, v2, weight = map(int, input().split())
        graph[v1][v2] = weight
        graph[v2][v1] = weight
    # print(graph)

    '''
    시작점이 0이 아닐 수도?
    그럼 시작점마다 MST 함수 돌려서 가중치 합 비교
    최종 가장 작은 값이 정답
    
    => 아니 시작점이 누구든 최소신장트리는 같은 형태로 나오니까? 반복문 돌릴 필요 X
    '''

    # for start in range(V + 1):
    #     tmp = make_MST(start)
    #     if result > tmp:
    #         result = tmp

    result = make_MST(0)

    print(f'#{tc}', result)
