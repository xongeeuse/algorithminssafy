import sys
sys.stdin = open('input_a2.txt')

def is_possible(idx):
    x = 1
    while True:
        left, right = idx - x, idx + x
        if left < 0 or right >= N:
            return True
        if data[left] == 1 and data[right] == 1:
            return False
        x += 1

    return True

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N개의 칸, M: 왼쪽에서 M번째 기준 칸
    data = list(map(int, input().split()))
    print(data)

    point_idx = M - 1

    for i in range(1, N):
        lpoint = point_idx - i
        rpoint = point_idx + i
        if 0 <= lpoint:
            if is_possible(lpoint):
                result = i
                break
        if 0 <= rpoint:
            if is_possible(rpoint):
                result = i
                break

    print(result)