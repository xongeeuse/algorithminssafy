def is_square(arr):
    n = len(arr)

    top = left = n
    bottom = right = -1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                top = min(top, i)
                left = min(left, j)
                bottom = max(bottom, i)
                right = max(right, j)

    if bottom - top != right - left:
        return False

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if arr[i][j] != '#':
                return False

    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    result = 'yes' if is_square(arr) else 'no'
    print(f'#{tc} {result}')