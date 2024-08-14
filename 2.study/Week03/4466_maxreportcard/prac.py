# 선택정렬
arr = [7, 5, 2, 9, 4]
N = len(arr)

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)