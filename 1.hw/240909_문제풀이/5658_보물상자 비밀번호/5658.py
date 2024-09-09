import sys
sys.stdin = open('input.txt')

def rotate(data):
    for i in range(N):
        tmp = ''
        for j in range(i, i + N // 4):
            tmp += data[j % N]
        passwords.add(tmp)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())        # N개의 숫자, K번째로 큰 수
    data = input()
    passwords = set()

    rotate(data)

    passwords = sorted(list(passwords), reverse=True)
    # print(passwords)
    result = passwords[K - 1]
    print(f'#{tc}', int(result, 16))
