import sys
sys.stdin = open('input.txt')

# 중위순회
def inorder(node):

    if tree[node]:                  # 왼쪽 자식 있으면 탐색
       inorder(tree[node][0])

    tree_inorder.append(node)       # 해당 정점 탐색

    if len(tree[node]) == 2:        # 오른쪽 자식 있으면 탐색
        inorder(tree[node][1])

# 중회순회 결과에서 루트(1번), N//2번 인덱스 찾기
def solution(tree_inorder):

    for i in range(len(tree_inorder)):
        if tree_inorder[i] == 1:        # 루트 인덱스 찾아서 [0]에 넣기
            result[0] = i
        if tree_inorder[i] == N//2:     # N//2번 인덱스 [1]에 넣기
            result[1] = i
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    tree_inorder = [0]
    result = [0, 0]

    # 이진트리 기본 구조 만들기
    for i in range(1, N//2 + 1):
        tree[i].append(i * 2)
        if i * 2 + 1 <= N:
            tree[i].append(i * 2 + 1)

    print(tree)
    inorder(node=1)
    print(f'#{tc}', *solution(tree_inorder))
