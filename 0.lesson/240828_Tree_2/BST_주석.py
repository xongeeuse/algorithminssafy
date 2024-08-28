'''
7
3 5 1 2 7 4 -5
'''

# 트리의 노드를 나타내는 클래스
# 각 노드는 자신이 가진 값(key)과 왼쪽, 오른쪽 자식 노드를 가집니다.
class Node:
    def __init__(self, key):
        self.key = key  # 노드가 가진 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

# 이진 탐색 트리(Binary Search Tree)를 관리하는 클래스
# 트리는 숫자를 특정 규칙에 따라 정리해서 저장하는 자료구조입니다.
class BinarySearchTree:
    def __init__(self):
        self.root = None  # 트리의 시작점인 루트(root) 노드를 초기화합니다.

    # 트리에 새로운 값을 추가하는 함수
    def insert(self, key):
        if self.root is None:  # 트리가 비어 있다면
            self.root = Node(key)  # 새 값을 루트 노드로 만듭니다.
        else:
            self._insert(self.root, key)  # 트리가 비어 있지 않다면, 적절한 위치에 삽입합니다.

    # 새로운 값을 적절한 위치에 삽입하기 위해 재귀적으로 호출되는 함수
    def _insert(self, node, key):
        if key < node.key:  # 새 값이 현재 노드의 값보다 작으면
            if node.left is None:  # 왼쪽 자식이 없으면
                node.left = Node(key)  # 새 값을 왼쪽 자식으로 만듭니다.
            else:
                self._insert(node.left, key)  # 왼쪽 자식이 있으면 그 쪽으로 가서 다시 비교합니다.
        else:  # 새 값이 현재 노드의 값보다 크면
            if node.right is None:  # 오른쪽 자식이 없으면
                node.right = Node(key)  # 새 값을 오른쪽 자식으로 만듭니다.
            else:
                self._insert(node.right, key)  # 오른쪽 자식이 있으면 그 쪽으로 가서 다시 비교합니다.

    # 트리에서 특정 값을 찾는 함수
    def search(self, key):
        return self._search(self.root, key)  # 루트부터 시작해서 값을 찾습니다.

    # 특정 값을 찾기 위해 재귀적으로 호출되는 함수
    def _search(self, node, key):
        if node is None or node.key == key:  # 찾고자 하는 값이 현재 노드에 있거나, 노드가 없다면
            return node  # 현재 노드를 반환합니다. (값을 찾으면 해당 노드를 반환, 못 찾으면 None 반환)
        if key < node.key:  # 찾는 값이 현재 노드의 값보다 작으면
            return self._search(node.left, key)  # 왼쪽으로 가서 다시 찾습니다.
        else:  # 찾는 값이 현재 노드의 값보다 크면
            return self._search(node.right, key)  # 오른쪽으로 가서 다시 찾습니다.

    # 트리의 값을 정렬된 순서대로 출력하기 위한 함수 (중위 순회)
    def inorder_traversal(self):
        self._inorder_traversal(self.root)  # 루트부터 시작해서 순서대로 값을 출력합니다.

    # 중위 순회를 위해 재귀적으로 호출되는 함수
    def _inorder_traversal(self, node):
        if node:  # 현재 노드가 존재할 때만 실행합니다.
            self._inorder_traversal(node.left)  # 왼쪽 자식을 먼저 방문
            print(node.key, end=' ')  # 현재 노드의 값을 출력
            self._inorder_traversal(node.right)  # 오른쪽 자식을 나중에 방문

# 사용자 입력을 받아 트리 생성
N = int(input())  # 입력받은 값의 개수
arr = list(map(int, input().split()))  # 입력받은 값들을 리스트로 변환

bst = BinarySearchTree()  # 이진 탐색 트리 생성

for num in arr:  # 입력받은 값들을 하나씩 트리에 추가
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회 결과를 출력 (작은 값부터 큰 값 순서대로)

# 특정 값 탐색 예제
key = 5
result = bst.search(key)  # 트리에서 5를 찾아봅니다.
if result:
    print(f"\n키 {key} 찾음.")  # 5를 찾으면 출력
else:
    print(f"\n키 {key} 못 찾음.")  # 못 찾으면 출력
