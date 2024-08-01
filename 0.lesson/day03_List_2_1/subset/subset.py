# # 비트를 이용한 부분집합 구하기
#
# bit = [0] * 4
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit)
#
#
# # 간결하게 부분집합 생성하는 방법
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)            # n : 원소의 개수
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=",")
#         print()
#     print()


# 비트 이용 추가 설명
arr = [1, 2, 3]
n = len(arr)            # 배열의 길이
    
subsets = []                # 모든 부분 집합을 저장할 리스트
for i in range(1 << n):     # 모든 가능한 부분 집합을 생성하기 위한 반복문 2 ** n
    subset = []                 # 현재 부분 집합을 저장할 리스트
    for j in range(n):      # 각 요소에 대해 포함 여부를 결정하기 위한 반복문
        if i & (1 << j) :   # i의 j번째 비트가 1인지 확인
            subset.append(arr[j])
    subsets.append(subset)

print(subsets)





# 연습
# arr = [1, 2, 3]
# n = len(arr)
#
# subsets = []
# for i in range(1 << n):
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#     subsets.append(subset)
# print(subsets)











