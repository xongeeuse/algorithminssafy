import sys
sys.stdin = open('input.txt')
'''
완전 이진 트리
인접 리스트 안 만들고
인덱스 이용해서 리스트로만 접근
'''

def inorder(node):
    left = node * 2
    right = node * 2 + 1
    if left <= N:
        inorder(left)
    tree_inorder.append(node)
    if right <= N:
        inorder(right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 노드의 개수
    tree = list(range(N + 1))
    tree_inorder = [0]
    inorder(node=1)
    result = [0, 0]
    for i in range(1, N + 1):
        if tree_inorder[i] == 1:
            result[0] = i
        if tree_inorder[i] == N // 2:
            result[1] = i
    print(f'#{tc}', *result)