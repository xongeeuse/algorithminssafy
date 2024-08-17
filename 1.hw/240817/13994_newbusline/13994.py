import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # N: 노선의 수
    stops = [0] * 1001      # 0번 정류장은 무시
    for _ in range(N):
        bustype, start, end = map(int, input().split())
        stops[start] += 1
        stops[end] += 1
        for i in range(start + 1, end):
            if bustype == 1:            # 일반 버스의 경우
                stops[i] += 1
            elif bustype == 2:          # 급행 버스의 경우
                if start % 2 == 0:      # 출발 정류장의 번호가 짝수면
                    if i % 2 == 0:
                        stops[i] += 1
                else:                   # 홀수면
                    if i % 2 == 1:
                        stops[i] += 1
            else:                       # 광역 급행 버스의 경우
                if start % 2 == 0:      # 짝수면
                    if i % 4 == 0:
                        stops[i] += 1
                else:                   # 홀수면
                    if i % 3 == 0 and i % 10 != 0:
                        stops[i] += 1
    result = 0
    for stop in stops:
        if result < stop:
            result = stop

    print(f'#{tc}', result)
