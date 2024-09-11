# path = []
#
# def KFC(x):
#     if x == 3:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
#
# KFC(0)
#
#

path = []           # 경로를 기록할 리스트
used = [0] * 7      # 1 ~ 6 숫자의 사용 여부를 기록할 리스트

def recur(level):

    # 1. 기저 조건?
    if level == 3:      # 종료 조건 : 3개를 뽑은 경우
        print(path)
        return

    # 2. 후보군을 반복하면서
    for i in range(1, 7):       # 1 ~ 6 후보군

        # i가 이미 뽑혔다면, continue 해라
        if used[i]:
            continue


        # 재귀 호출 전 : 경로 기록 + 사용 기록
        used[i] = 1
        path.append(i)

        # 다음 재귀 호출(파라미터 전달)
        recur(level + 1)

        # 돌아왔을 때 - 사용했던 경로 삭제 + 사용 여부 초기화
        path.pop()
        used[i] = 0


recur(0)    # 호출 : 시작점을 같이 전달해주는 경우가 많음