arr1 = [0] * 3

# 2차원 배열
# row(행). column(열)
arr2 = [[0] * 3 for _ in range(2)]   # 2행 짜리니까 range(2)
# arr = [[0] * 3] * 2   # 이렇게 하시면 안됩니다 절대!

# print(arr1)
# print(*arr1)

# for i in range(2):
#     print(*arr2[i])  # i번째 행 전체를 의미, *으로 언팩

for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = ' ')
    print()


# 배열 순회 - 행 우선 순회
# 모든 요소의 합 구하기
S = 0
for i in range(N):
    for j in range(M):
        S += arr[i][j]


# 행의 합 중 최댓값 구하기

max_v = 0   # 초기값은 조심해서 설정할 것! 문제의 조건에 맞는 적절한 값!
for i in range(N):
    S = 0
    for j in range(M):
        S += arr[i][j]

        if max_v < S:
            max_v = S

# 배열 순회 - 열 우선 순회
for j in range(m):  # 열
    for i in range(n):  # 행
        f(arr[i][j])

# 가로 세로 길이가 같은 경우 아래도 가능
for i in range(m):
    for j in range(n):
        f(arr[i][j])
        f(arr[j][i])

# 배열 순회 - 지그재그 순회?
for i in range(n):
    for j in range(m):
        f(arr[i][j + (m-1-2*j) * (i%2)])






