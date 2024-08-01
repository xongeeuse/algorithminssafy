import sys
sys.stdin = open('input.txt')

def binary_search(end, key):
    l = 1
    r = end
    c = r // 2
    cnt = 0
    while (1):
        cnt += 1
        if c == key:
            return cnt
        elif c > key:
            r = c
        elif c < key:
            l = c
        c = (r + l) // 2


T = int(input())
for testcase in range(1, T + 1):
    p, a, b = map(int, input().split())

    if binary_search(p, a) == binary_search(p, b):
        print(f'#{testcase}', 0)
    elif binary_search(p, a) > binary_search(p, b):
        print(f'#{testcase}', 'B')
    else:
        print(f'#{testcase}', 'A')