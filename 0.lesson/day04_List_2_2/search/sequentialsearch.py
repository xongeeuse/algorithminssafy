# 검색 - 순차 검색

# 정렬되어 있지 않읂 경우
arr = [1, 3, 7, 11, 5, 9]

def sequential_search(a, n, key):   # a : 정렬할 리스트, n : 리스트의 길이, key : 찾을 값
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n :
        return i
    else:
        return -1

print(sequential_search(arr, len(arr), 5))


# 정렬되어 있는 경우
arr2 = sorted(arr)      # [1, 3, 5, 7, 9, 11]

def sequential_search_2(a, n, key):
    # while문 쓴 경우
    i = 0
    while i < n and a[i] == key:  # 무조건 인덱스 검색 먼저! 순서 바뀌면 단축평가로 인한 에러 발생할 수도
        return i
    else:
        return -1
    
    # for문 쓴 경우
    # for i in range(n - 1):
    #     if a[i] == key :
    #         return i
    #     elif a[i] > key:
    #         return -1
    # return -1

print(sequential_search_2(arr2, len(arr), 5))