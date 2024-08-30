import sys
sys.stdin = open('input.txt')
from collections import deque

def dedupe(data):
    stack = []

    while data:
        d = data.popleft()
        if stack:                   # 스택이 비어있지 않으면
            if d == stack[-1]:      # d와 스택 마지막 요소 비교해서
                stack.pop()         # 같으면 pop
                continue
        stack.append(d)             # 다르거나 스택이 비어있으면 stack에 넣기

    return len(stack)


T = int(input())
for tc in range(1, T+1):
    data = deque(input())
    print(f'#{tc}', dedupe(data))





# # 예전 풀이
# # 더 간단한 듯
# def search_repetition(data):
#     stack = []
#     for d in data:
#         if len(stack) == 0 or stack[-1] != d:       # 스택이 비어 있거나, top이 d와 다르면
#             stack.append(d)                         # 스택에 d를 넣어라
#         elif stack[-1] == d:                        # top이 d라면
#             stack.pop()                             # 스택에서 d를 꺼내라
#
#     return len(stack)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     data = list(input())
#
#     print(f'#{tc}', search_repetition(data))
