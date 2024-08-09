# 집합[1, 2, 3]에서 모든 순열 생성하기
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)



# 비트연산자 이용 모든 부분집합 구하기
A = [1, 2, 3, 4]
n = len(A)

for i in range(1 << n):             # 총 부분집합의 개수 2**n
    subset = []
    for j in range(n):              # 원소의 개수만큼 반복
        if i & (1 << j):            # i의 j번째 요소가 1이면
            subset.append(A[j])     # 부분집합에 j번 요소를 넣어라
    print(subset)