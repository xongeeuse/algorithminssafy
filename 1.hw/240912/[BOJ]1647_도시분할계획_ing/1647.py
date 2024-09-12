import sys
sys.stdin = open('input.txt')

'''
최소 신장 트리 + 다익스트라?
두 개의 마을?.....어떻게 마을 두 개로?
=> 최소 신장 트리 만들고 그 중 마지막에 추가된 간선(==가장 비용이 많이 드는 간선)을 끊어주면 최소 비용으로 두 개의 마을 만들기 가능
=> 시간 초 과...!

'''

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x, y = find_set(x), find_set(y)

    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())            # 집의 개수 N, 길의 개수 M
edge = []
parent = [i for i in range(100001)]
for _ in range(M):
    v1, v2, weight = map(int, input().split())
    edge.append((weight, v1, v2))
edge.sort()
print(edge)

cnt, total, last = 0, 0, 0
for weight, v1, v2 in edge:
    if find_set(v1) == find_set(v2):
        continue

    union(v1, v2)
    cnt += 1
    total += weight
    last = weight

    if cnt == N - 1:
        break

print(total - last)