import sys
# sys.stdin = open('input1.txt')

'''
N개의 활동 구역
왼쪽에서 오른쪽으로 진행
먹이를 먹으면 K칸 이동
+ 추가 먹이 못 먹으면 K번째 칸에 멈추기
최대 몇 번째 칸까지 이동할 수 있는가

먹이 O : 1 / 먹이 X : 0
첫번째 구역에는 항상 먹이 있음
'''

def solution(data, K):
    cnt = 0                             # 몇 번째 칸까지 이동했는지 확인할 변수
    idx = 1                             # 현재 탐색 중인 index

    while cnt < K:                      # cnt가 최대 이동 칸수보다 작은 동안
        idx += 1                        # idx 늘려가며 탐색 진행
        if idx == N - 1:                # 마지막 idx 도달 시 탐색 종료
            break

        if data[idx] == 1:              # 탐색 중인데 먹이가 또 있으면 cnt 리셋
            cnt = 0
        else:
            cnt += 1                    # 먹이 없으면 cnt + 1
    return idx


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N: 활동 구역 개수, K: 먹이 먹고 이동하는 최대 칸 수
    data = list(map(int, input().split()))
    result = solution(data, K)
    print(f'#{tc}', result)