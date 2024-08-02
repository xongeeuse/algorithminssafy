import sys
sys.stdin = open('input.txt')

T = int(input())
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
str_to_num = {}


for _ in range(1, T+1):
    tc, n = input().split()
    words = input().split()
    max_value = 9

    count_list = [0] * len(nums)

    for word in words:
        count_list[str_to_num[word]] += 1

    result = []

    for l, c in enumerate(count_list):
        result.extend(([nums[i]] * c))

    print(tc)
    print(' '.join(result))