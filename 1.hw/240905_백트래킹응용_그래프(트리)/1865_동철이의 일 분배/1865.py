def solution(row, possibility):
    global mx

    if mx >= possibility:           # 이미 기존 최댓값보다 작으면 백트래킹
        return

    if row == N:                    # 모두 선택했다면
        if mx < possibility:        # 기존 최댓값과 비교해서 재할당
            mx = possibility
        return

    for j in range(N):
        if visited[j]:              # 이미 선택된 일이면 넘어가
            continue

        # 선택된 적 없으면
        visited[j] = 1                                          # 방문 체크하고
        solution(row + 1, possibility * data[row][j])           # 다음 선택하러 고고

        # 돌아오면 방문 체크 해제하고
        visited[j] = 0
    return



T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # N명의 사람, N개의 일
    # data = [list(map(int, input().split())) for _ in range(N)]
    # 데이터 받아올 때 0.01 곱한 상태로 받기
    # 함수 내부 연산 줄어드니까 시간 단축에 도움이 될까요?
    data = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    mx = 0

    solution(0, 100)

    print(f'#{tc} {mx:.6f}')
    # print(f'#{tc}', format(mx, ".6f"))