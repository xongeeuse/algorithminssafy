import sys
sys.stdin = open('input1.txt')

'''
#1 1
#2 5
#3 5
'''

def find_mx_len(data):
    global mx
    for i in range(N):
        cnt = 1                             # 구간 길이 초기값 1으로 설정
        for j in range(1, N):
            if i - j < 0 or i + j >= N:     # 범위 밖이면 브레이크
                break
            if data[i - j] == data[i + j]:  # 양쪽 값이 같으면 구간 길이에 2씩 더하기
                cnt += 2
            else:
                break
        if mx < cnt: mx = cnt



T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # N: 배열의 길이
    data = list(input())
    # M = len(data)         # 길이 또 왜 쟀어..
    mx = float('-inf')
    find_mx_len(data)
    print(f'#{tc}', mx)

