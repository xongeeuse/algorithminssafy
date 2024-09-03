import sys
sys.stdin = open('input.txt')
'''
완탐 + 재귀?
카드 바꾸는 부분을 함수로 해서 교환 횟수 다 쓸 때까지 재귀 호출?
교환횟수 0 되면 결과값 리스트에 넣고
최종 비교해서 최댓값 출력
땡떙
'''

'''
주어진 숫자판 이용해서 모든 순열 생성
가장 큰 배열이 교환 횟수 내에서 만들어질 수 있는지 확인
가능하면 그 금액이 최대상금
안되면 다음 순열에 대해 확인 계속...
'''



# 숫자판 교환 결과 => 상금으로 변환
def cards_to_money(cards):
    money = 0
    cards = list(map(int, cards))
    for i in range(M):
        money += cards[i] * 10 ** (M - 1 - i)
    return money



def solution(cards, cnt):
    # global result

    while True:
        if cnt == 0:
            money = cards_to_money(cards)
            result.append(money)
            return

        for i in range(M):
            for j in range(i + 1, M):
                # if j == i:
                #     continue
                cards[i], cards[j] = cards[j], cards[i]
                solution(cards, cnt - 1)
                cards[i], cards[j] = cards[j], cards[i]



T = int(input())
for tc in range(1, T + 1):
    data, N = input().split()         # data: 숫자판의 정보, N: 교환 횟수
    N = int(N)
    data = list(data)
    M = len(data)
    result = []

    print(data)
    solution(cards = data[:], cnt= N)

    print(f'#{tc}', max(result))
