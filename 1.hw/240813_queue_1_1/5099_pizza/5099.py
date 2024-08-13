import sys
sys.stdin = open('input.txt')

from collections import deque

def find_last_pizza(data):
    # fire = deque(data[:N])

    pizzas = deque(data)
    fire = deque()
    for i in range(N):
        fire.append(pizzas.popleft())

    while fire:
        pizza = fire.popleft()
        if pizza[1] < 2:
            result = pizza[0]
            if pizzas:
                fire.append(pizzas.popleft())
        else:
            fire.append((pizza[0], pizza[1]//2))

    return result




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())                                # N: 화덕 크기, M: 피자 개수
    data = list(enumerate(map(int, input().split()), start=1))      # ([0]피자 번호, [1]피자에 뿌려진 치즈의 양)

    print(f'#{tc}', find_last_pizza(data))