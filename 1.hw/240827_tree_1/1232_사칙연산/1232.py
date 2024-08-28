import sys
sys.stdin = open('input.txt')
'''
# 1
1. 일단 중위순회 순서대로 나열하고
2. +, - 먼저 계산
3. *, / 계산
근데 너무 비효율적인 것 같지만 일단 고
땡땡 틀렸습니다!
'''

'''
# 2
후위순회해서 숫자 먼저 받고 => 후위표기식 순서
앞에서부터 스택에 넣으면서 계산하기
'''

# 트리 ==> 후위표기식 순서로 변환
def postorder(node):

    if tree[node][1]:                                   # 노드의 인접리스트가 있으면
        postorder(tree[node][1][0])                     # 왼쪽 자식에 대해 탐색 진행
    if len(tree[node][1]) > 1:                          # 인접리스트 길이가 1보다 크면 == 오른쪽 자식이 있다면
        postorder(tree[node][1][1])                     # 오른쪽 자식에 대해 탐색 진행
    organized.append(tree[node][0])                     # 해당 노드 방문(?)



# 후위표기식 계산하는 함수
def calculator(organized):
    stack = []

    for o in organized:
        if o.isdecimal():
            stack.append(float(o))      # 실수형으로 계산하고
            continue

        # elif len(stack) < 2 :
        #     return 'error'

        n2 = stack.pop()
        n1 = stack.pop()

        if o == '+':
            n3 = n1 + n2
        elif o == '-':
            n3 = n1 - n2
        elif o == '*':
            n3 = n1 * n2
        elif o == '/':
            n3 = n1 / n2
        stack.append(n3)

    return int(stack.pop())             # 결과값만 정수로 반환



T = 10
for tc in range(1, T + 1):
    N = int(input())
    # 람다함수 이용해서 숫자라면 int 변환하고 아니라면 그 값 그대로 받아오는 방법도 있음
    # 이렇게 데이터를 받아온다면 연산자인지 피연산자인지 구분할 때 type 사용할 수 있음
        # if type(arr[node][1]) == type(''): 이렇게!
    # arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    tree = [[] for _ in range(N + 1)]
    organized = []
    for _ in range(N):
        temp = input().split()
        tree[int(temp[0])].append(temp[1])                      # 해당 번호 인덱스의 [0]에 정점의 정보 넣기(연산자 or 양의 정수)
        tree[int(temp[0])].append(list(map(int, temp[2:])))     # [1]에 해당 정점의 자식 넣기, 자식 없으면 [] 삽입

    postorder(1)
    result = calculator(organized)

    print(f'#{tc}', result)