import sys
sys.stdin = open('input.txt')

T = int(input())

# 함수 안 쓰고 만들어보기
for tc in range(1, T+1):
    data = input()
    stack = []
    lbracket, rbracket = '(', ')'
    result = -1

    for d in data:
        if d == lbracket:           # d가 '('면 스택에 넣어라
            stack.append(d)

        elif d == rbracket:         # d가 ')'인데
            if len(stack) == 0:     # 스택이 비어있으면
                result = -1         # 결과 -1
                break
            stack.pop()             # 짝 맞으면 스택의 마지막 '('를 제거

    else:                           # for문 break하지 않고 끝까지 완료했을 시 실행!
        if len(stack) == 0:
            result = 1

    print(result)



# 강사님 풀이 듣고 한 것!
# def bracket_check(data):
#     stack = []
#     matching = {')':'('}
#     result = -1
#
#     for d in data:
#         if d in matching.values():
#             stack.append(d)
#         elif d in matching.keys():
#             if not stack or stack[-1] != matching[d]:
#                 return result
#
#             stack.pop()
#
#     if len(stack) == 0:
#         result = 1
#
#     return result
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     data = input()
#
#     print(f'#{tc}', bracket_check(data))