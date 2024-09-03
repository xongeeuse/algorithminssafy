# 부분집합 생성하기
data = ['MIN', 'CO', 'TIM']
arr = ['X', 'O']
N = len(data)
path = []

# 기존 방법
# for i in range(1 << N):               # 만들 수 있는 집합의 총 개수
#     subset = []
#     for j in range(N):                # 모든 원소의 개수에 대해
#         if i & (1 << j):
#             subset.append(data[j])
#     print(subset)


# 완전탐색 이용
# def print_name():
#     print('{', end= ' ')
#     for i in range(N):
#         if path[i] == 'O':
#             print(data[i], end=' ')
#     print('}')
#
#
# def run(lev):
#     if lev == 3:
#         print_name()
#         return
#
#     for i in range(2):          # 데려간다 안간다
#         path.append(arr[i])
#         run(lev + 1)
#         path.pop()
#
# run(0)

# binary counting 이용
def get_sub(target):
    for i in range(N):
        if target & 0x1:
            print(data[i], end = ' ')
        target >>= 1

for target in range(1 << N):
    print('{', end=' ')
    get_sub(target)
    print('}')