'''
주사위 3개 던지는 경우의 수 중복순열
세 눈금의 합이 10 이하인 경우 출력
'''

path = []
used = [0] * 7              # 중복 없어야 하는 경우 이용

def permutation(level, total):
    global cnt
    
    # 기저조건
    if level == 3:
        # print(path)
        if total <= 10:
            cnt += 1
        return
    
    # 백트래킹 가지치기 : 이미 10을 넘는 경우의 수는 계산할 필요 X
    if total >= 10:
        return


    for i in range(1, 7):
        # if used[i]:
        #     continue

        used[i] = 1
        path.append(i)

        permutation(level + 1, total + i)

        path.pop()
        used[i] = 0

cnt = 0
permutation(0, 0)
print(cnt)