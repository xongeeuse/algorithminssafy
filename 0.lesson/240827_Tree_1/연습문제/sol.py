import sys
sys.stdin = open('input.txt')

def search(node):   # 해당 노드 정보를 토대로 왼쪽, 오른쪽 조사
    if node != 0:   # node 값이 0이 아니라면 (0번 노드 없음)
        # print(node, end=' ')        # 전위
        search(tree[node][0])       # 왼쪽 조사
        # print(node, end=' ')        # 중위
        search(tree[node][1])       # 오른쪽 조사
        print(node, end=' ')        # 후위ㅋ





V = int(input())            # V : 전체 노드의 수
arr = list(map(int, input().split()))

# tree 정보를 입력할 수 있도록
# tree 리스트의 idx 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 -> 왼쪽 자식
# tree[parent] 위치의 리스트의 1번째 -> 오른쪽 자식
tree = [[0, 0] for _ in range(V + 1)]

# for i in range(len(arr)//2):
#     parent, child = arr[i * 2], arr[i * 2 + 1]
#     if tree[parent][0] == 0:
#         tree[parent][0] = child
#     else: tree[parent][1] = child


for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i + 1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else: tree[parent][1] = child

search(1)