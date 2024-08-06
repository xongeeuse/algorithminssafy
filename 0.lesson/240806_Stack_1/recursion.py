# 재귀 호출
# 모든 배열 원소에 접근하기
def f(i, N):        # i: 현재 인덱스, N: 배열의 크기
    if i == N:
        return
    else:
        print(arr[i])
        return f(i+1, N)

arr = range(5)
N = len(arr)
f(0, N)

# 배열에 v가 있으면 1, 없으면 0을 리턴
def f2(i, N, v):
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f2(i+1, N, v)

print(f2(0, N, 3))
print(f2(0, N, 5))
