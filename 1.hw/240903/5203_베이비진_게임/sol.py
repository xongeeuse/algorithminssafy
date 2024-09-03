import sys
sys.stdin = open('input.txt')

'''
0~9의 번호가 적힌 카드 6장 입력
3장의 카드가 연속적 번호인 경우 = RUN
3장의 카드가 동일한 번호인 경우 = TRIPLET
6장의 카드가 run과 triplet으로만 구성된 경우 'Baby-gin'
완전탐색으로 baby-gin 여부 판단하기
'''

'''
1. 6장의 카드로 만들 수 있는 모든 순서 나열하기 => 순열 생성
2. run, triplet
'''


'''
012가 런일때 345가 트리플렛, 런
012가 트리플렛일때 345가 트리플렛, 런
'''


def is_babygin(path):
    global cnt

    babygin = 0  # babygin == 2면 베이비진!
    # Run 확인
    if path[0] == path[1] == path[2] or path[3] == path[4] == path[5]:
        babygin += 1
        # Triplet 확인
        if path[1] == path[0] + 1 and path[2] == path[1] + 1 or path[4] == path[3] + 1 and path[5] == path[4] + 1:
            babygin += 1

    if babygin == 2:
        cnt += 1



def permutation(card, lev):
    # global cnt

    if lev == 6:
        is_babygin(path)            # 생성된 순열에 대해 베이비진 확인
        # if cnt == 1:              # 베이비진이였다면 cnt == 1
        return

    for i in range(6):
        if used[i]:
            continue

        used[i] = 1  # i 사용 체크 하고
        path.append(card[i])  # 순열에 i번째 카드 넣기

        permutation(card, lev + 1)  # 다음 카드 뽑으러 재귀 호출

        if cnt == 1:
            return

        path.pop()  # 돌아와서 이전 카드 삭제해주고
        used[i] = 0  # i 사용 체크 해제


T = int(input())
for tc in range(1, T+1):

    data = list(map(int, input().split()))
    A, B = [], []

    for i in range(12):
        if i % 2 != 0:
            B.append(data[i])
        else:
            A.append(data[i])


    path = []
    used = [0] * 6
    cnt = 0

    permu = []
    permutation(A, 0)
    permutation(B, 0)
    print(cnt)
