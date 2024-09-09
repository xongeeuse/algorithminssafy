import sys
sys.stdin = open('input.txt')
'''
N가지 재료를 반으로 나누는 경우의 수? 조합..
123, 456 으로 나눈다면
12 13 21 23을 다 더한 값이 synergy_A?
'''

def dfs(cnt, previous, synergy_A, synergy_B):
    global mn

    if cnt == N:
        # A - B 절대값 비교해서 재할당하고 리턴
        if mn > abs(synergy_A - synergy_B):
            mn = abs(synergy_A - synergy_B)
        return

    for j in range(N):
        if visited[j]:
            continue

        visited[j] = 1

        if cnt < N / 2:
            # A 변수에 더하기
            dfs(cnt + 1, j, synergy_A + data[previous][j], synergy_B)
            visited[j] = 0

        else:
            # B 변수에 더하기
            dfs(cnt + 1, j, synergy_A, synergy_B + data[previous][j])
            visited[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # N: 식재료의 수
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    mn = float('inf')

    for i in range(N):
        visited[i] = 1
        dfs(0, i, 0, 0)
        visited[i] = 0

    # 이게 왜 전자카트랑 같다는 거야?
    # 아 그냥 절반 선택하면 나머지 절반은 자동으로 선택되니까

    print(f'#{tc}', mn)

