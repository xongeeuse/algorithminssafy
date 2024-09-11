'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     parents[x] = find_set(parents[x])
#     return parents[x]


# 걍 한 번에 리턴해도 똑같은거 아닌가?
def find_set(x):
    if parent[x] != x:                      # 본인이 대표자가 아니라면
        parent[x] = find_set(parent[x])     # 대표자로 업데이트 해주고

    return parent[x]                        # 대표자 리턴


def union(x, y):
    x , y = find_set(x), find_set(y)

    if x == y:          # 대표자가 같다? == 같은 그룹이다 == 합칠 필요 X
        return
    if x < y:
        parent[y] = x   # 더 작은 루트 노드를 부모로!
    else:
        parent[x] = y


V, E = map(int, input().split())
edge = []
for _ in range(E):
    v1, v2, weight = map(int, input().split())
    edge.append([v1, v2, weight])
edge.sort(key=lambda x : x[2])      # 가중치 기준 오름차순으로 정렬
parent = [i for i in range(V + 1)]
print(parent)

cnt = 1
total = 0
for v1, v2, weight in edge:
    if find_set(v1) != find_set(v2):
        cnt += 1
        union(v1, v2)
        total += weight
        if cnt == V:
            break
print(total)