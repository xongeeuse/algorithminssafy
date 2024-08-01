import sys
sys.stdin = open('input.txt')

T = int(input())

def binary_search(l, r, key):
    cnt = 0
    while l <= r :
        cnt += 1
        c = (l + r) // 2
        if c == key:
            return cnt
        elif c < key:
            l = c + 1
        elif c > key:
            r = c - 1
    return cnt

for testcase in range(1, T+1):
    P, A, B = map(int, input().split()) # P : 책의 전체 쪽 수, A, B : A와 B가 각각 찾을 쪽 번호

    if binary_search(1, P, A) < binary_search(1, P, B):
        print(f'#{testcase}', 'A')
    elif binary_search(1, P, A) > binary_search(1, P, B):
        print(f'#{testcase}', 'B')
    else: print(f'#{testcase}', '0')
