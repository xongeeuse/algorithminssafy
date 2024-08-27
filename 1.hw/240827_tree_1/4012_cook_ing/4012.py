import sys
sys.stdin = open('input.txt')

def ():


T = int(input())
for tc in range(1, T + 1):
    N = int(input())            # N: 식재료의 수
    data = [list(map(int, input().split())) for _ in range(N)]
    mn = float('inf')
    print(data)
