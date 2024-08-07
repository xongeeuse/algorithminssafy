import sys

sys.stdin = open('input.txt')

"""
memoization을 활용해서 구현 
시간 복잡도: O(N^2) - 좀 더 빠름 

개선된 재귀와 동일하게 코드를 작성하나
기존 행을 계산한 적 있으면 해당 값을 사용하며, 사용한 적이 없으면 값을 계산한 다음에 memo에 저장한다.
"""
def pascal_triangle(n, memo={}):
    if n == 1:
        return [1]

    if n in memo:
        return memo[n]

    prev_row = pascal_triangle(n - 1, memo)
    new_row = [1]

    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])

    new_row.append(1)
    memo[n] = new_row
    return new_row


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    memo = {}
    for i in range(1, N + 1):
        row = pascal_triangle(i, memo)
        print(' '.join(map(str, row)))
