import sys

sys.stdin = open('input.txt')

"""
DP를 활용해서 구현 
시간 복잡도: O(N^2) - 좀 더 더 빠름 

memoization과 달리 가장 윗 줄부터 계산하면서 깊게 들어간다.
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    # 파스칼 삼각형을 저장할 2차원 배열을 생성
    triangle = [[0] * N for _ in range(N)]

    # 모든 행의 첫 번째 열과 마지막 열을 1로 초기화
    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1

    # 파스칼 삼각형의 값을 아래값부터 게산하면서 올라감
    # for i in range(2, N):
    for i in range(N):
        for j in range(1, i):
            # 이전 행의 2개의 값을 합쳐서, 현재 행에 저장
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    for i in range(N):
        # 각 행에서 i행이면 i번째까지만 출력
        # 왜냐면 나머지는 0으로 채웠기 때문
        print(' '.join(map(str, triangle[i][:i + 1])))
