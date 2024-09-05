'''
원소의 합이 10인 부분집합 모두 출력하시오.
'''

def dfs(level, sum, idx):
    if sum == target_sum:
        print(visited)

    if sum > 10:
        return

    for i in range(idx, N):
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
target_sum = 10
visited = []

dfs(0, 0, 0)