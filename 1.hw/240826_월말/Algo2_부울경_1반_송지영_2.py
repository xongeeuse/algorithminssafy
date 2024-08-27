import sys
sys.stdin = open('input2.txt')
'''
#1 5
'''

'''
N명의 외계인
줄 서는 순서에 따라 가스발생 위험도 달라짐

1.
순열 생성해서 모든 경우의 수 비교하기
근데 순열 어떻게 만들더라?

2.
열 방문 리스트 만들고
행 기준으로 탐색 진행
열 방문 안했으면 방문 체크하고 tmp에 data[i][j]값 더하기
모든 행에 대해 탐색 했으면 min값과 비교 후 재할당?

3.
아 이거 배열최소합이랑 같은건데.. dfs 백트래킹 문제...
'''

def solution(visited, current_sum, cnt, row):
    global mn

    if cnt == N - 1:                        # 탐색 끝났으면
        if mn > current_sum:                # 기존 mn값과 비교 후 재할당
            mn = current_sum
        return

    if current_sum >= mn:                   # 현재 합이 이미 최솟값 이상이면 백트래킹
        return

    for j in range(N):
        if j != row and visited[j] == 0:
            visited[j] = 1
            solution(visited, current_sum + data[row][j], cnt + 1, row=j)       # j행에 대해 탐색 진행, cnt + 1
            # 돌아오면 방문 체크 해제하고...
            visited[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # N: 외계인의 수
    data = [list(map(int, input().split())) for _ in range(N)]
    mn = float('inf')
    cnt = 0
    solution(visited=[0] * N, current_sum=0, cnt=0, row=0)
    print(f'#{tc}', mn)




