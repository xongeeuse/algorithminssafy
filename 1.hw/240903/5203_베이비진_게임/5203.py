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


def is_babygin(player):
    # Triplet인지 확인
    for j in range(N):
        if player[j] == 3:
            return True

    # Run인지 확인
    for k in range(8):
        if player[k] and player[k + 1] and player[k + 2]:
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    N = 10                      # 카드 숫자의 범위 0 ~ 9
    A, B = [0] * N, [0] * N     # 카드 개수 카운트할 리스트 생성
    winner = 0                  # 0: 무승부, 1: A, 2: B

    for i in range(len(cards)):     # 주어진 카드들에 대해
        if not i % 2:               # 홀수 차례면
            A[cards[i]] += 1        # A 리스트의 해당 리스트에 +1
            # if sum(A) < 3:        # 카드 3장 모이기 전에는 베이비진 확인 하지 말라고 넣었으나 굳이?
            #     continue
            if is_babygin(A):
                winner = 1
                break

        else:
            B[cards[i]] += 1
            # if sum(B) < 3:
            #     continue
            if is_babygin(B):
                winner = 2
                break

    print(f'#{tc}', winner)
