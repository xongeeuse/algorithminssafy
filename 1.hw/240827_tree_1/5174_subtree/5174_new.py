import sys

sys.stdin = open('input.txt')


def count_node(N):
    global result

    if not tree[N]:         # 자식 노드가 없으면
        return              # 탐색 종료

    for x in tree[N]:
        result += 1
        count_node(x)



T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())            # E: 간선의 개수, N: 루트
    data = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]           # 부모 index에 자식 노드 번호 저장
    result = 1                                  # 루트를 서브 트리 개수에 포함하고 시작

    for i in range(0, len(data), 2):
        tree[data[i]].append(data[i + 1])       # parent: data[i], child: data[i + 1]
    # print(tree)

    count_node(N)
    print(f'#{tc}', result)



