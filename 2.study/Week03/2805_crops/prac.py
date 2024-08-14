arr = [[1, 4, 0, 5, 4, 1, 1],
       [4, 4, 2, 5, 0, 1, 1],
       [0, 2, 0, 3, 2, 1, 1],
       [5, 1, 2, 0, 4, 1, 1],
       [5, 2, 2, 1, 2, 1, 1],
       [5, 2, 2, 1, 2, 1, 1],
       [5, 2, 2, 1, 2, 1, 1]]
N = len(arr)

for i in range(N//2):
    for x in range((N//2)-1-i, -1, -1):
        arr[i].pop()
        arr[i].pop(0)

for i in range((N//2)+1, N):
    for x in range(1, i -(N//2)+1):
        arr[i].pop()
        arr[i].pop(0)


print(arr)