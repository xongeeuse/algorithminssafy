import sys
sys.stdin = open('input.txt')

def binary_search(target, left, right, direction):
    global result
    if left == right:
        if target == A[left]:
            result += 1
        return

    mid = (left + right) // 2
    if target == A[mid]:
        result += 1
        return

    elif target < A[mid]:
        if direction == 'L':
            return
        binary_search(target, left, mid - 1, direction = 'L')

    else:
        if direction == 'R':
            return
        binary_search(target, mid + 1, right, direction = 'R')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N, M: A, B 리스트에 속한 정수의 개수
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    result = 0

    for num in B:
        binary_search(num, 0, N - 1, 0)

    print(f'#{tc}', result)

