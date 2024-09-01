import sys
sys.stdin = open('input.txt')
'''
data = 완전이진트리를 중위순회한 결과
레벨이 i인 빌딩의 개수 = 2**i
레벨이 i인 빌딩의 번호 = range((2**i), 2**i + 개수)
'''

def inorder(node):
    global tree_inorder

    left = node * 2
    right = node * 2 + 1
    if left <= N:
        inorder(left)

    tree_inorder.append(node)

    if right <= N:
        inorder(right)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())                                    # 완전이진트리의 깊이
    data = list(map(int, input().split()))              # 완전이진트리를 중위순회한 결과
    N = 2**K - 1                                        # 노드의 총 개수

    tree = list(range(N + 1))                   # 인덱스 참조 위해 완전이진트리 만들고
    tree_inorder = [0]
    inorder(1)                                  # 중위순회하기
    # print(tree_inorder)

    real_map = [0] * (N + 1)
    for i in range(1, N + 1):
        real_map[tree_inorder[i]] = data[i - 1]
    # print(real_map)

    for i in range(K):
        for k in range(2**i):
            print(real_map[2**i + k], end=' ')
        print()


    # print(data)