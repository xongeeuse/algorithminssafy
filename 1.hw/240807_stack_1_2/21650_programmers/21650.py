# def solution(progresses, speeds):
#     answer = []
#     left = []
#
#     # 각 프로젝트의 남은 기간 계산
#     for i in range(len(progresses)):
#         cnt = 0
#         while True:
#             progresses[i] += speeds[i]
#             cnt += 1
#             if progresses[i] >= 100:
#                 left.append(cnt)
#                 break
#
#     # 리턴 값 맞추기 1 - tc 3개만 맞음
#     # result = 1
#     # for i in range(len(left)-1):
#     #     if left[i] >= left[i+1]:
#     #         result += 1
#     #     elif left[i] < left[i+1]:
#     #         answer.append(result)
#     #         result = 1
#     # answer.append(result)
#
#     # 리턴 값 맞추기 2 - Fail / 스택 이용하려 했으나 반복문 틀리게 돌아감
#     cnt = 0
#     while left:
#         temp = left.pop(0)
#         cnt += 1
#         if len(left) == 0:
#             answer.append(cnt)
#             break
#         elif temp >= left[0]:
#             left.pop(0)
#             cnt += 1
#         elif temp < left[0]:
#             answer.append(cnt)
#             cnt = 0
#
#     return answer
#

# My SOL
def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0

    while progresses:
        if progresses[0] + speeds[0] * day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                day += 1
    answer.append(cnt)
    return answer


# another SOL 2
# ?????
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]

print(solution(progresses = [93, 30, 55], speeds= [1, 30, 5]))
