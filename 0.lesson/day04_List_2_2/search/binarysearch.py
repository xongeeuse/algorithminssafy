# 검색 - 이진 검색

arr = [2, 4, 7, 9, 11, 19, 23]

def binary_search(a, N, key):
    start = 0
    end = N - 1
    while start <= end :
        mid = (start + end) // 2
        if a[mid] == key :
            return True
        elif a[mid] > key :
            end = mid - 1
        else : start = mid + 1
    return False


print(binary_search(arr, len(arr), 19))
print(binary_search(arr, len(arr), 5))


# 재귀 함수를 이용한 이진 검색
# 교재 참고해서 다시 작성해보기!

def binary_search2(a, low, high, key):      # 0부터 100까지 찾을 때 low : 0, high : 100
    pass
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binary_search2(a, low, mid - 1, key)
        elif a[mid] < key:
            return binary_search2(a, mid + 1, high, key)

print(binary_search2(arr, len(arr), 19))
print(binary_search2(arr, len(arr), 5))




