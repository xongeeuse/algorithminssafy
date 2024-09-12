'''
3 1
4 2
4 4
'''

# 1

def permutation(x):
    if x == M:
        print(*permu)
        return

    for i in range(1, N + 1):
        if i not in permu:
            permu.append(i)
            permutation(x + 1)
            permu.pop()

N, M = map(int, input().split())
permu = []
permutation(0)



# 2 강사님 방법
N, M = map(int, input().split())

def permu(acc, arr):
    if len(arr) == M:
        result.append(acc)

    for idx in range(len(arr)):
        new = arr[idx]
        arr[idx], arr[-1] = arr[-1], arr[idx]
        permu(acc + [new], arr[:-1])
        arr[idx], arr[-1] = arr[-1], arr[idx]

arr = [i for i in range(1, N + 1)]
result = []
permu([], arr)
result.sort()

for r in result:
    print(*r)

