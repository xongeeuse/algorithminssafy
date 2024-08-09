#

def f(i, K):                # bit[i]를 결정하는 함수
    if i == K:              # 모든 요소에 대해 결정하면
        s = 0               # 부분집합의 합 저장할 변수
        for j in range(K):
            if bit[j]:      # bit[j]가 0이 아니면
                print(a[j], end=' ')
                s += a[j]
        print(':', s)       # 부분집합을 한 행에 출력

    else:
        # bit[i] = 1
        # f(i+1, K)
        # bit[i] = 0
        # f(i+1, K)
        for j in [1, 0]:
            bit[i] = j
            f(i+1, K)

a = range(1, 4)
N = len(a)
bit = [0] * N

f(0, N)