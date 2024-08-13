import sys
sys.stdin = open('input.txt')

def bracket_check(data):
    stack = []
    bracket_dict = {')': '(', '}': '{'}

    for d in data:
        if d in bracket_dict.values():
            stack.append(d)
        elif d in bracket_dict.keys():
            if len(stack) == 0 or stack[-1] != bracket_dict[d]:
                return 0
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    data = input()
    print(f'#{tc}', bracket_check(data))

