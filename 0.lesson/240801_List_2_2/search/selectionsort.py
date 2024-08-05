# 선택 정렬

def selection_sort(arr, N):             # arr : 정렬대상, N : 크기
    for i in range(N-1) :               # 주어진 구간에 대해 기준 위치 i를 정하고
        min_idx = i                     # 최솟값 위치를 기준 위치로 가정
        for j in range(i+1, N):         # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 구간의 최솟값을 기준 위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


A = [64, 25, 10, 22, 11]
B = [5, 4, 3, 1, 2]

print(selection_sort(A, len(A)))
print(selection_sort(B, len(B)))