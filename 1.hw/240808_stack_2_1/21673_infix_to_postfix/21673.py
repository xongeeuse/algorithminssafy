import sys
sys.stdin = open('input.txt')

# 중위표기법에서 후위표기법 변환하는 함수
def infix_to_postfix(data):
    nums = list(map(str, range(10)))
    operators = {'+' : 1,
                 '-' : 1,
                 '*' : 2,
                 '/' : 2}
    stack = []
    postfix = ''

    for d in data:
        if d in nums:                                       # d가 숫자면
            # d = int(d)
            postfix += d                                    # d를 postfix 에 넣어라
        else:                                               # d가 연산자이고
            if not stack:                                   # 스택이 비어있으면
                stack.append(d)                             # 스택에 d를 넣어라
            elif operators[d] <= operators[stack[-1]]:      # d의 우선순위가 top 연산자의 우선순위보다 높거나 같으면
                postfix += stack.pop()                      # top을 postfix에 넣고
                stack.append(d)                             # 스택에 d를 넣어라
            else:                                           # d의 우선순위가 top 연산자의 우선순위보다 낮으면
                stack.append(d)                             # 스택에 d를 넣어라
    while stack:                                            # 모든 d에 대한 탐색이 끝나고 스택에 요소가 남아 있으면
        postfix += stack.pop()                              # top을 순서대로 postfix에 넣어라

    return postfix



T = int(input())

for tc in range(1, T+1):
    data = input()

    print(f'#{tc}', infix_to_postfix(data))

