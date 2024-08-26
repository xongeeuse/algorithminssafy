'''

가능한 순열 생성해서


'''

N = 3
data = [[0, 7, 2],
        [6, 0, 5],
        [4, 3, 0]]
arr = [0, 1, 2]

def permutation(arr):
    for i in range(N):
        temp = []
        if arr[i] not in temp:
            temp.append(arr[i])
            for j in range(N):
                if arr[j] not in temp:
                    temp.append(arr[j])
                    for k in range(N):
                        if arr[k] not in temp:
                            temp.append(arr[k])
        print(temp)

permutation(arr)