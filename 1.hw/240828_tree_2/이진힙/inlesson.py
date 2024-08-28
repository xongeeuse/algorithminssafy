import sys
sys.stdin = open('input.txt')

# from queue import PriorityQueue # 우선순위 큐

# 삽입을 위한 함수
def enqueue(target):            # target: 삽입한 위치
                                # 단순히 tree에 삽입 대상을 집어 넣는 게 아니라 삽입한 후
                                # 부모 노드와 내 노드의 크기를 비교해서
                                # 부모 노드의 값이 내 노드의 값보다 크다면, 위치 스왑
    while target // 2:
        parent = target // 2
        if tree[target] <= tree[parent]:
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(N, arr)
    tree = [0]
    last_node = 0
    for item in arr:
        tree.append(item)
        last_node += 1
        enqueue(last_node)

    result = 0
    parent = last_node // 2
    while parent >= 1:
        result += tree[parent]
        parent //= 2

    print(f'#{tc}', result)