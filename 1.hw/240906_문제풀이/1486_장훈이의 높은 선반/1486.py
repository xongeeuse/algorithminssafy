import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())            # N: 점원 수, B: 탑의 높이
    data = list(map(int, input().split()))      # 점원들의 키
    result = []

    for i in range(1 << N):
        tmp = 0
        for j in range(N):
            if i & (1 << j):
                tmp += data[j]
        if tmp >= B:
            result.append(tmp)

    result.sort()

    ans = result[0] - B

    print(f'#{tc}', ans)