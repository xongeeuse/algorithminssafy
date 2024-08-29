import sys
sys.stdin = open('input.txt')
'''
소수점 아래 12자리 이내인 이진수로 표시 가능하면 0.제외 나머지 숫자 출력
초과하면 'overflow' 출력
'''

# 소수 10진법 => 2진법으로 변환
def dec_to_bin(N):
    global result

    while True:
        N *= 2                   # 계속 2 곱해주기
        result += str(int(N))    # 정수부분은 결과에 담아주기

        if N == 1:               # 1이면 중단
            break

        N -= int(N)              # 정수부분 빼주고 반복 계속

    if len(result) > 12:         # 결과가 12자리 이상이면 overflow
        return 'overflow'

    return result               # 아니면 결과 반환



T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    result = ''
    print(f'#{tc}', dec_to_bin(N))
