import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # bubblesort
    # for i in range(N):
    #     for j in range(N-i-1):
    #         if nums[j] > nums[j+1]:
    #             nums[j], nums[j+1] = nums[j+1], nums[j]


    # selectionsort
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if nums[min_idx] > nums[j]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]


    print(f'#{tc}', *nums)