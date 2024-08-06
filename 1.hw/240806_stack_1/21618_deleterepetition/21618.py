import sys
sys.stdin = open('input.txt')

def search_repetition(data):
    stack = []
    for d in data:
        if len(stack) == 0 or stack[-1] != d:       # 스택이 비어 있거나, top이 d와 다르면
            stack.append(d)                         # 스택에 d를 넣어라
        elif stack[-1] == d:                        # top이 d라면
            stack.pop()                             # 스택에서 d를 꺼내라

    return len(stack)

T = int(input())

for tc in range(1, T+1):
    data = list(input())

    print(f'#{tc}', search_repetition(data))
