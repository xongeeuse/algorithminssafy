import sys
sys.stdin = open('input.txt')

def solution(row, possiblity):
    global mx

    if mx > possiblity:
        return

    if row == N:
        if mx < possiblity: mx = possiblity
        return

    for j in range(N):
        if visited[j]:              # 이미 선택된 일이면 넘어가고
            continue

        # 선택된 적 없으면
        visited[j] = 1              # 방문 체크하고
        solution(row + 1, possiblity * data[row][j] * 0.01)           # 다음 선택하러 고고

        # 돌아오면 방문 체크 해제하고
        visited[j] = 0



T = int(input())

for tc in range(1, T + 1):
    N = int(input())                        # N명의 사람, N개의 일
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    mx = -1

    solution(row= 0, possiblity= 1)
    mx = mx * 100
    # result = round(mx, 7)                       # 7번째 자리에서 반올림하고

    # print(f'#{tc}', format(result, ".6f"))      # 소수점 자리 맞춰서 출력하기
    print(f'#{tc}', format(mx, ".6f"))      # 소수점 자리 맞춰서 출력하기