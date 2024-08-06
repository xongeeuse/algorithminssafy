import sys
sys.stdin = open('input.txt')

def bracket_check(data):
    stack = []
    check_dict = {')':'(', '}':'{', ']':'['}

    for d in data:
        if d in check_dict.values():                            # d가 열린 괄호면
            stack.append(d)                                     # 스택에 넣어라
        elif d in check_dict.keys():                            # d가 닫힌 괄호일 때    
            if len(stack) == 0 or stack[-1] != check_dict[d]:   # 스택이 비었거나, top과 짝이 맞지 않으면
                return 0                                        # 0 반환
            stack.pop()                                         # 짝이 맞으면 top 제거

    if len(stack) == 0:                                         # 모든 문자 순회 후 스택이 비었다면 == 짝이 다 맞았다는 것!
        return 1                                                # 1 반환
    else:                                                       # 아니라면
        return 0                                                # 0 반환


T = int(input())

for tc in range(1, T+1):
    data = input()
    print(f'#{tc}', bracket_check(data))