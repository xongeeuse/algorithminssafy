'''
서로소 집합, 상호배타 집합 : 서로 중복 포함된 원소가 없는 집합 = 교집합이 없다!
두 집합 간에 공통 원소가 하나도 없을 때, 이 두 집합이 서로소 집합!
서로소 집합은 연결해도 사이클이 생기지 않음!
그래프에서 사이클의 유무 검출은 중요 포인트!
'''

'''
최종 정리!
서로소집합? 사이클 검출할 때 쓴다
사이클 검출하려면? 서로 같은 집합이면 안된다
disjoint를 이용해서 각 원소들을 집합화하고
union을 이용해서 집합을 만들고 find를 이용해서 대표자끼리 비교 => 같은 집합인지 비교!
'''

# 대표자(=부모) 인덱스 저장할 리스트 생성
parent = [0] * (N + 1)

def make_set(x):
    parent[x] = x

# 대표자 찾는 함수
def find_set(x):
    if x == parent[x]:              # x 본인이 대표자라면
        return x                    # x값 반환
    return find_set(parent[x])      # 같아질 때 까지 대표자 찾아 올라가기

# x, y 포함하는 두 집합을 통합하는 연산
def union(x, y):
    px = find_set(x)        # x 대표자 나와
    py = find_set(y)        # y 대표자 나와

    if px < py:             # 대표끼리 비교해서
        parent[y] = px      # 작은 쪽을 부모로 둘거야(누구를 부모로 둘지는 개발자 마음)
    else:
        parent[x] = py

'''
서로소 집합의 최적화
<Path compression>
=> Find-set을 행하는 과정에서 모든 노드들이 직접 root를 가리키도록!
    특정 노드에서 루트까지의 경로를 찾아가면서 부모 노드를 갱신
'''
# 최적화 후
def find_set(x):
    if x != parent[x]:                          # 대표자가 아닌 경우
        parent[x] = find_set(parent[x])         # 루트 찾아 올라가고, 재귀를 나오면서 루트 값으로 갱신
    return parent[x]



'''
<Rank를 활용한 Union>
=> 각 노드는 자신을 루트로 하는 subtree의 높이를 rank로 저장
    두 집합을 합칠 때 rank가 낮은 집합을 높은 집합에 붙인다
'''

# 각 노드 별 랭크(높이)를 저장할 리스트 필요
parent = [0] * (N + 1)
rank = [0] * (N + 1)

# 최적화 후
def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:                    # 대표자가 같다면(같은 그룹) 합칠 필요 없으니까 다른 경우에만 진행
        if rank[px] > rank[py]:     # 랭크(높이)가 작은 쪽의 대표자를 큰 쪽으로 변경
            parent[py] = px
        elif rank[px] < rank[py]:
            parent[px] = py

        # 이 부분 이해 못 함...
        else:                       # 랭크가 같다면
            parent[py] = px         # 적절히 조절하면서? 편향트리 안 만들 수 있음?
            rank[px] += 1           # 임의의 한 쪽 높이에 + 1해 주고 붙여줌

