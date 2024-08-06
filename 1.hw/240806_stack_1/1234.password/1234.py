import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, data = input().split()
    N = int(N)
    stack = []

    for d in data:
        if len(stack) != 0 and stack[-1] == d:
            stack.pop()
            continue
        stack.append(d)

    print(f'#{tc}', ''.join(stack))