import sys
sys.stdin = open('input.txt')
'''
그리디?
- 적재용량이 가장 큰 트럭에 가장 무거운 컨테이너 싣기

1. 컨테이너, 트럭 모두 무게 오름차순으로 정렬
2. 트럭이 있는 동안 반복문
3. 마지막 요소부터 팝해서 짝지어 주기
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())                # N: 컨테이너의 수, M: 트럭의 수
    container = list(map(int, input().split()))     # N개 컨테이너의 무게
    truck = list(map(int, input().split()))         # M개 트럭의 적재용량
    
    # 오름차순으로 정렬하고
    container.sort()
    truck.sort()

    total = 0
    while truck:                        # 트럭이 있는 동안
        if not container:               # 옮길 컨테이너가 없으면
            break                       # 종료

        truck_now = truck[-1]                   # 현재 남은 가장 적재용량 큰 트럭
        container_now = container.pop()         # 현재 남은 가장 무거운 컨테이너
        if truck_now >= container_now:          # 적재 가능하면
            truck.pop()                         # 트럭 꺼내주고
            total += container_now              # 컨테이너 싣고 총량에 무게 더하기

    print(f'#{tc}', total)