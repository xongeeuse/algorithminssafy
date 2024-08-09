def f(i, k, s, t):          # i: 원소, k: 집합의 크기, s: i-1까지 고려된 합, t: 목표
    global cnt
    global fcnt
    fcnt += 1               # 함수 호출 횟수 비교해볼것! backtracking vs dfs (가지치기 있 vs 없)

    # 가지치기 하는 경우
    if s > t:               # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:            # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1            # 카운트 추가 후 리턴
        return
    elif i == k:            # 모든 원소 고려 끝나면
        return

    # # 가지치기 없는 경우
    # if i == k:
    #     if s == t:
    #          cnt += 1

    else:
        bit[i] = 1          # A[i] 포함
        f(i + 1, k, s + A[i], t)
        bit[i] = 0          # A[i] 미포함
        f(i + 1, k, s, t)







A = range(1, 11)
N = len(A)

key = 10
cnt = 0
bit = [0] * N
fcnt = 0
f(0, N, 0, key)
print(cnt, fcnt)