import sys
sys.stdin = open('input.txt')

def traversal(node):
    # if len(result) == N:              # 없어도 돌아가네
    #     return

    if adjL[node][1]:                   # 해당 정점의 인접리스트가 있으면 왼쪽 탐색 진행
        traversal(adjL[node][1][0])

    result.append(adjL[node][0])        # 해당 정점 탐색

    if len(adjL[node][1]) == 2:
        traversal(adjL[node][1][1])     # 인접정점이 2개면 오른쪽 탐색 진행




T = 10
for tc in range(1, T+1):
    N = int(input())                        # N : 총 정점 수
    adjL = [[] for _ in range(N + 1)]
    for _ in range(N):
        temp = input().split()
        adjL[int(temp[0])].append(temp[1])                      # adjL[i][0]: 해당 정점의 문자
        adjL[int(temp[0])].append(list(map(int, temp[2:])))     # adjL[i][1]: 해당 정점의 인접리스트 저장

    result = []
    traversal(1)
    print(f'#{tc}', ''.join(result))
