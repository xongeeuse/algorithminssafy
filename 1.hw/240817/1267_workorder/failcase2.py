import sys
sys.stdin = open('input.txt')

############################################ tc 5/10 맞음~!

def search_starts():
    notstarts = []
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if i in adjL[j]:
                notstarts.append(i)
    notstarts = list(set(notstarts))
    starts = []
    for i in range(1, V + 1):
        if i not in notstarts and adjL[i]:
            starts.append(i)
    return starts


def bfs(starts, adjL):
    q = []
    visited = [0] * (V + 1)
    result = []
    for start in starts:
        result.append(start)
        visited[start] = 1                  # 시작점 방문체크
        for v in adjL[start]:               # 시작점의 인접리스트
            if visited[v] == 0:
                q.append(v)                 # 다음 순서 큐에 넣기

        while q:                            # 큐가 있는 동안
            tmp = q.pop(0)                  # 첫번째 팝해서
            for each in firstL[tmp]:
                if visited[each] == 0:
                    break
            else:                           # 위 for문을 break하고 나오지 않았을 때만 실행
                result.append(tmp)
                visited[tmp] = 1            # 방문 체크하고
                for v in adjL[tmp]:         # 현재 탐색 지점의 인접리스트
                    if visited[v] == 0:
                        q.append(v)         # 다음 순서 큐에 넣기

    return result


T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V 정점의 개수, E 간선 개수
    data = list(map(int, input().split()))
    adjL = [[] for _ in range(V + 1)]  # 0번 인덱스는 항상 비어있음, 무시!
    firstL = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        adjL[v1].append(v2)
        firstL[v2].append(v1)
    starts = search_starts()
    print(f'#{tc}', *bfs(starts, adjL))
