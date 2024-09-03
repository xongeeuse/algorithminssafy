import sys
sys.stdin = open('input.txt')

# 7번까지 출력하고 계속 돌아가는 중~

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



# # 숫자판 교환 결과 => 상금으로 변환
# def cards_to_money(cards):
#     money = 0
#     cards = list(map(int, cards))
#     for i in range(M):
#         money += cards[i] * 10 ** (M - 1 - i)
#     return money



def prize_money(cnt):
    global result

    if cnt == N:                                    # 주어진 횟수만큼 교환 끝났다면
        result = max(result, int(''.join(data)))
        # tmp_result = int(''.join(data))
        # if ans <= tmp_result:                      # 현재 결과와 tmp 비교해서 재할당
        #     ans = tmp_result
        return

    for i in range(M):
        for j in range(i + 1, M):
            data[i], data[j] = data[j], data[i]     # i, j 카드 바꿔주고

            tmp = int(''.join(data))                # 숫자판 상태 저장
            if (cnt, tmp) not in visited:           # 지금까지 지나온 결과가 아니라면
                visited.add((cnt, tmp))             # (현재까지 교환 횟수, 숫자판 상태) 방문기록 해주고

                prize_money(cnt + 1)                # 다음 카드 바꾸러 고고

            # 돌아오면 다시 카드 상태 원위치
            data[i], data[j] = data[j], data[i]



T = int(input())
for tc in range(1, T + 1):
    data, N = input().split()         # data: 숫자판의 정보, N: 교환 횟수
    N = int(N)
    data = list(data)
    M = len(data)
    visited = set()
    result = 0
    prize_money(cnt= 0)

    print(f'#{tc}', result)

'''
15**10
같은값 안바꿈
중간과정에서, 답이 나왔으면  멈춘다
(최대값이 나왔다면) + (남은 교환횟수가 짝수면) 끝
+
최대값이 나왔는데 + 남은 교환횟수가 홀수면 (중복된 숫자있으면) 끝

최대값 나옴. 남은 교환횟수 홀수. 중복숫자 없음 => ...
654321   1
654312

665432   1
665432

123456
654321

15**6'''