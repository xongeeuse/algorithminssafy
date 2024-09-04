arr = [2, 4, 7, 9, 11, 19, 23]

def binary_search(target):
    low = 0
    high = len(arr) - 1
    cnt = 0         # 탐색 횟수

    while low <= high:                      # low가 high 이하인 동안 반복
        mid = (low + high) // 2             # mid는
        cnt += 1

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:             # 왼쪽을 확인해야 한다면 high 값을 mid - 1로 설정
            high = mid - 1
        else:                               # 오른쪽을 확인해야 한다면 low 값을 mid + 1로 설정
           low = mid + 1

    return '못 찾음', cnt

print(binary_search(9))
print(binary_search(2))
print(binary_search(20))