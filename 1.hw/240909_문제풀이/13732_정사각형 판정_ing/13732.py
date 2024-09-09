import sys
sys.stdin = open('input.txt', 'r')

'''
하나가 정사각형 아니라고 No 리턴하고 끝내지 말고
남은 # 중에 정사각형이 있는지 확인해야 하나?
'''

def is_square(data):
    for i in range(N):
        cnt = 0                         # 정사각형 한 변의 길이 후보
        for j in range(N):
            if data[i][j] == '#':       # 전체 범위 탐색하면서 # 이면 카운트 시작
                cnt += 1

            if data[i][j] != '#' or j == N - 1:     # #이 아니거나, 행의 마지막 인덱스라면
                if cnt <= 1:                        # 카운트 확인하고 1 이하면 0으로 리셋
                    cnt = 0
                    continue
                for k in range(i + 1, i + cnt):         # 2 이상이라면 다음 행부터 정사각형 확인
                    for l in range(j, j - cnt, -1):     # 인덱스 확인해보자
                        if k < 0 or k >= N or l < 0 or l >= N:
                            return 'no'
                        if data[k][l] != '#':
                            return 'no'
                else:
                    return 'yes'


    return 'no'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    result = is_square(data)
    print(f'#{tc}', result)