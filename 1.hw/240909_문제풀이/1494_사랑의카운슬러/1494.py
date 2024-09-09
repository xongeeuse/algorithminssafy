import sys
sys.stdin = open('input.txt')
'''
V = (x, y) = x * x + y * y
모든 지렁이들을 매칭시키고 소개팅을 주선하되, 각 지렁이들이 움직인 벡터를 합하여 그 크기가 최소가 되도록!
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = []
    for _ in range(N):
        x, y = map(int, input().split())
        data.append((x, y))
    print()
    print(data)