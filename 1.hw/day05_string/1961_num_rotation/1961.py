import sys
sys.stdin = open('input.txt')

# 틀림
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if i < j:
#                 data[i][j], data[j][i] = data[j][i], data[i][j]
#
#     print(data)




# another SOL
T = int(input())

# 90도 회전하는 함수
def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)
    rot_270 = rotation(rot_180, N)

    print("#{}".format(tc))
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])), end=" ")
        print()


# SOLSOL
# 90도 회전하는 함수
def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(input().split() for _ in range(n))

    arr90 = rotation(arr, n)
    arr180 = rotation(arr90, n)
    arr270 = rotation(arr180, n)

    print(f"#{test_case}")
    for i, j, k in zip(arr90, arr180, arr270):
        print(f"{''.join(i)} {''.join(j)} {''.join(k)}")