import sys
sys.stdin = open('input.txt')
'''
1. 일단 중위순회 순서대로 나열하고
2. +, - 먼저 계산
3. *, / 계산
근데 너무 비효율적인 것 같지만 일단 고
'''

'''
땡땡 틀렸고
후위순회해서 숫자 먼저 받고 => 후위표기식 순서
앞에서 부터 pop하면서 계산하기
'''

# 트리 ==> 후위표기식 순서로 변환
def postorder(node, tree):

    if tree[node][1]:
        postorder(tree[node][1][0], tree)
    if len(tree[node][1]) > 1:
        postorder(tree[node][1][1], tree)
    organized.append(tree[node][0])



# 후위표기식 계산하는 함수
def calculator(organized):
    stack = []

    for o in organized:
        if o.isdecimal():
            stack.append(int(o))
            continue

        elif len(stack) < 2 :
            return 'error'

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
        stack.append(int(n3))

    return stack[0]



T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    organized = []
    for _ in range(N):
        temp = input().split()
        tree[int(temp[0])].append(temp[1])              # 해당 번호 인덱스의 [0]에 정점의 정보 넣기(연산자 or 양의 정수)
        tree[int(temp[0])].append(list(map(int, temp[2:])))     # [1]에 해당 정점의 자식 넣기, 자식 없으면 [] 삽입

    postorder(1, tree)
    result = calculator(organized)

    print(f'#{tc}', result)