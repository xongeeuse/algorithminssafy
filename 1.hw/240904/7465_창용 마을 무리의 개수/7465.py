import sys
sys.stdin = open('input.txt')

'''
그래프 1번 노드부터 시작해서 탐색 진행
방문체크하면서 넘어가기
모든 노드가 방문되지 않았는데 순회가 끝나면 +1
방문되지 않은 지점부터 다시 탐색 진행

=> 새로운 무리 시작할 때 카운트 하는 걸로 변경
'''


#[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def find_group(node):
    global result

    visited[node] = 1

    for v in adjL[node]:
        if visited[v]:
            continue
        find_group(v)

        '''
        한 점에서 시작한 순회가 끝나고 새로 시작할 때 무리의 수(result)에 + 1 해줘야 함
        근데 왜 계속 돌아가는지
        재귀 위치가 뭔가 잘못됨 확인필요!
        '''


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())            # N: 사람 수, M: 관계 수
    adjL = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    result = 0
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    for i in range(1, N + 1):       # 모든 사람에 대해 반복
        if visited[i]:              # 이미 무리에 속한 사람이면 다음으로
            continue
        result += 1                 # 새로운 사람이면 result(무리) + 1 해주고
        find_group(i)               # 탐색 진행

    print(f'#{tc}', result)