import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    tc = int(input())
    data = list(map(int, input().split()))
    scores = [0] * 101
    for d in data:
        scores[d] += 1
    mx, ans = 0, 0
    for i in range(1, 101):
        if mx <= scores[i]:
            mx = scores[i]
            ans = i

    print(f'#{tc}', ans)