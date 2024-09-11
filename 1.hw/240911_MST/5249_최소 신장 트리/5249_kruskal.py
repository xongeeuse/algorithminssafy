import sys
sys.stdin = open('input.txt')

# kruskal 방식으로
def find_set(x):
    if parent[x] != x:                      # x의 부모(대표자)가 x가 아니라면
        parent[x] = find_set(parent[x])     # 최종 부모를 찾아서 parent[x] 업데이트 해주고
    return parent[x]                        # 부모 값 리턴


def union(x, y):
    x, y = find_set(x), find_set(y)

    if x == y:                    # x, y의 대표자가 같다면 합칠 필요 없어~!
        return
    if x < y:                       # 번호가 작은 쪽을 부모로 합치기
        parent[y] = x
    else:
        parent[x] = y
    return


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())     # V: 마지막 노드 번호(0 ~ V번), E: 간선 개수
    edge = []                           # 간선 정보 담을 리스트 생성
    parent = [i for i in range(V + 1)]  # 대표자(부모) 정보 담을 리스트 생성
    for _ in range(E):
        v1, v2, weight = map(int, input().split())
        edge.append([v1, v2, weight])
    edge.sort(key=lambda x: x[2])           # 가중치(weight) 기준 오름차순으로 정렬

    cnt, total = 0, 0
    for v1, v2, weight in edge:
        if find_set(v1) != find_set(v2):
            union(v1, v2)
            cnt += 1
            total += weight
        if cnt == V + 1:
            break

    print(f'#{tc}', total)