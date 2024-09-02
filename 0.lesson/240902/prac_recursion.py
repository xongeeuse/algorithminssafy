# path = []
# # N = 3
#
#
# def run(lev):
#     if lev == N:
#         print(path)
#         return
#
#     for i in range(1, 4):
#         path.append(i)
#         run(lev + 1)
#         path.pop()
#
# N = int(input())
# run(0)


def KFC(x):
    # 1. 기저조건(종료조건
    if x == 6:]po
        return

    # 2. 다음 재귀 호출 전
    print(x, end=' ')

    # 3. 재귀 호출 (현재 값에 무슨 수식을 적용해서 넘겨줄까?)
    KFC(x + 1)  # 다음 재귀 호출에서는 현재보다 x 값이 1 커야한다.

    # 4. 호출하고 돌아왔을 때때
    print(x, end=' ')

KFC(0)