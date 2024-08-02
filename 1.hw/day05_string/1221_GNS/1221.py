import sys
sys.stdin = open('input.txt')

T = int(input())
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T+1):
    tc, N = (input().split())
    N = int(N)
    counts = [0] * len(nums)
    # tc : #테스트 케이스 번호, N : 단어의 개수
    data = list(input().split())
    temp = [0] * N

    # data 숫자로 변환
    for i in range(N):
        for j in range(len(nums)):
            if data[i] == nums[j]:
                data[i] = j

    # 숫자 카운팅 정렬
    for x in data:
        counts[x] += 1

    for i in range(1, len(nums)):
        counts[i] += counts[i - 1]

    for i in range(N-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    # 정렬한 데이터 다시 외계어로 변환
    for i in range(N):
        for j in range(len(nums)):
            if temp[i] == j:
                temp[i] = nums[j]

    result = ' '.join(temp)
    print(tc)
    print(result)