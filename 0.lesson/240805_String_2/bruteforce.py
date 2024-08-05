# 고지식한 알고리즘 brute force
# 1
t = 'TTTTTABC'
p = 'TTA'
N = len(t)
M = len(p)
cnt = 0
for i in range(N-M+1):          # 비교 시작 위치
    for j in range(M):
        if t[i + j] != p[j]:
            break               # for j, 다음 글자부터 비교 시작
    else:                       # for j가 중단 없이 반복되면..
        cnt += 1                # 패턴 개수 1 증가
print(cnt)


# 2
def f(t, p):                    # 패턴 p와 일치하는 구간의 시작 인덱스 리턴, 없으면 -1 리턴
    N = len(t)
    M = len(p)

    for i in range(N - M +1):   # 비교 시작 위치
        for j in range(M):
            if t[i + j] != p[j]:
                break           # for j, 다음 글자부터 비교 시작
        else:                   # for j가 중단 없이 반복되면
            return i            # 패턴을 찾은 경우
    return -1

t = 'TTTTTABC'
p = 'TTA'

print(f(t, p))
