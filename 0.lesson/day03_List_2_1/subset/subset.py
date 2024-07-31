# 비트를 이용한 부분집합 구하기

bit = [0] * 4

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit)


# 간결하게 부분집합 생성하는 방법
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)            # n : 원소의 개수

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
        print()
    print()
