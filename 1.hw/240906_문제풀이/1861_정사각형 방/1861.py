import sys
sys.stdin = open('input.txt', "r")

# 22번 케이스 재귀 호출 깊이 초과해서 넣어줌..
# import sys
# sys.setrecursionlimit(10**7)

'''
그냥 반복문 2개로 끝내려면 오류 있음
다음 좌표 정하고 그 좌표 기준으로 다시 탐색해야 하니까 재귀로 돌려야 함

+ 시간 초과 나서 check 함수 추가
'''

# 탐색할 가치가 있는 시작점인지 판단하기 위한 함수
def check(i, j):
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        # if visited[ni][nj]:
        #     continue
        if data[ni][nj] == data[i][j] - 1:      # 근처에 본인보다 -1 작은 값이 있다면 그 곳이 더 유망하니까
            return False                        # 현재 시작점은 가지치기
    return True


def solution(i, j, visited):
    global tmp

    visited[i][j] = 1

    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if data[ni][nj] == data[i][j] + 1:  # 현재 방 번호보다 하나 큰 값이면
            tmp += 1
            solution(ni, nj, visited)       # 다음 좌표 기준 탐색하러 가기
            break


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    result = [0, 0]     # [방 번호, 최대 이동할 수 있는 방의 수]

    for i in range(N):
        for j in range(N):

            # 유망한 시작점이 아니라면 패스
            if not check(i, j):
                continue

            tmp = 1
            solution(i, j, visited=[[0] * N for _ in range(N)])
            if result[1] < tmp:
                result[0], result[1] = data[i][j], tmp

            elif result[1] == tmp:                  # 이동할 수 있는 방의 개수가 같다면
                if result[0] > data[i][j]:          # 방 번호가 작은 쪽으로 갱신
                    result[0] = data[i][j]

    print(f'#{tc}', *result)