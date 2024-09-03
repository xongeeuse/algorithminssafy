arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# # my SOL
# def get_sub(target):
#     global cnt
#     for i in range(N):
#         if target & 0x1:
#             subset.append(data[i])
#         target >>= 1
#     if len(subset) >= 2:
#         cnt += 1
#
# cnt = 0
# for target in range(1 << N):
#     subset = []
#     get_sub(target)
#
# print(cnt)



# 총 몇개의 bit가 1로 되어있는지 확인하는 함수
def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


result = 0
for tar in range(0, 1 << n):  # range(0, 8)
    if get_count(tar) >= 2:  # bit가 2개 이상 1 이라면,
        result += 1
print(result)


