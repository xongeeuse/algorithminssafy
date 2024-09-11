'''
그래프 vs 트리
- 사이클 존재 유무에 따라 구분될 수 있음, 그래프가 더 큰 개념, 트리가 그래프의 특수한 형태

신장트리(Spanning Tree)
- 사이클이 없고, 노드가 모두 이어져 있는 그래프
- N개의 정점, N - 1개의 간선

최소신장트리(Minimum Spanning Tree)
total cost의 값이 최소인..?
아래의 여러가지 알고리즘을 통해 구할 수 있음

- Kruskal 알고리즘(그리디 방식으로 접근해서 MST 만듦)
=> 간선을 하나씩 선택해서 MST를 찾는 알고리즘 => 하나씩 찾다보면 MST가 되지 않겠어??!
1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
2. 가중치가 가장 낮은 간선부터 선택
    - 두 대표자가 다르다면, 엣지를 최소 비용 집합에 추가
    - 두 대표자가 같다면, 사이클이 생성되므로 무시! 트리니까 사이클 생기면 안돼!!!!!!!!!!
3. N - 1개의 간선이 선택될 때까지 2번 과정 반복

가중치는 어떻게 부여되는..?................
'''

# KRUSKAL

def mst_kruskal(verrices, edges):
    mst = []
    n = len(vertices)
    ds = DisjointSet(vertices)

    for i in range(n + 1):
        ds.make_set(i)

    edges.sort(key=lambda x: x[2])      # 가중치 기준 정렬
    s, e, w = edge
    if ds.find_set