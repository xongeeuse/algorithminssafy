import sys
sys.stdin = open('input.txt')

"""
스택을 활용해서 구현
시간복잡도 O(N^2), 조금 빠름 (개선된 재귀보다 오버플로우 걱정이 덜해서 유리)
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    # 첫 번째 행은 항상 [1]
    prev_stack = [1]
    print(1)

    # 파스칼 삼각형은 1로 시작해서 1로 끝나고, 그 사이값은 이전 행의 두 값의 합으로 구성된다.
    # 첫 번째 줄은 이미 [1]로 세팅을 했기 때문에, 2번째 줄부터 진행
    for i in range(1, N):
        new_stack = [1]  # 새로운 행은 항상 1로 시작

        # 이전 행의 인접한 두 수를 더하여 새로운 행 생성
        # 2개씩 더하기 때문에, 윗 줄의 총 개수 - 1개 만큼 더해야 한다. ( 안그러면 터짐 )
        for j in range(len(prev_stack) - 1):
            new_stack.append(prev_stack[j] + prev_stack[j + 1])

        new_stack.append(1)  # 행의 마지막은 항상 1

        # 방금 생성한 파스칼 출력
        print(' '.join(map(str, new_stack)))

        prev_stack = new_stack  # 다음 반복을 위해 스택 업데이트
