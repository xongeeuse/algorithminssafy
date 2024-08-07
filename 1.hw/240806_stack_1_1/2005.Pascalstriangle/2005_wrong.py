import sys
sys.stdin = open('input.txt')

def pascal(N):                  # 파스칼의 삼각형 N번째 행 만드는 함수
    result = []

    result.append(1)            # 시작하는 1 넣고

    if N >= 3:                  # 중간값 N-2개 넣고
        for _ in range(N-2):
            result.append(N-1)

    if N != 1:                  # N이 1이 아닐 때만 마지막 1 넣어주기
        result.append(1)

    return result


def pascal_result(N):           # 합치기
    result = []
    for i in range(1, N+1):
        result.append(pascal(i))
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')

    for p in pascal_result(N):
        print(*p)