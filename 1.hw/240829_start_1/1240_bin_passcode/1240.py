import sys
sys.stdin = open('input.txt')

passcode_dict = {'0001101' : '0', '0011001' : '1', '0010011' : '2', '0111101' : '3', '0100011' : '4',
                 '0110001' : '5', '0101111' : '6', '0111011' : '7', '0110111' : '8', '0001011' : '9'}

# 패스코드 행 + 끝점 좌표 찾기
def find_code():
    global data
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1':
                data = data[i]
                return j

def is_correct(passcode):
    odd_sum = 0                         # 홀수 자리의 합을 받아줄 변수
    total = 0                           # 홀수 자리 합 * 3 + 짝수 자리 합 받아줄 변수
    result = 0                          # 모든 자리의 총 합
    for x in range(8):
        i = x + 1
        result += int(passcode[x])
        if i % 2 == 1:                  # 홀수 자리면 odd_sum에 값 더하기
            odd_sum += int(passcode[x])
        else:                           # 짝수 자리면 total에 값 더하기
            total += int(passcode[x])

    total += odd_sum * 3

    if total % 10 == 0:                  # total이 10의 배수면
        return result                    # 총 합 반환
    else:
        return 0    # 아니면 0 반환


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N x M 배열의 크기
    data = [input() for _ in range(N)]
    end = find_code()
    passcode = ''
    for j in range(end - 55, end + 1, 7):
        if data[j:j + 7] in passcode_dict:
            passcode += passcode_dict[data[j:j + 7]]

    # print(passcode)
    print(f'#{tc}', is_correct(passcode))