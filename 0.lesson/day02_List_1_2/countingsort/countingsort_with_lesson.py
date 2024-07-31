DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5    # DATA가 0~4까지의 정수

N = len(DATA)
TEMP = [0] * N

# 1단계 : DATA 원소 별 개수 세기
for x in DATA:                      # DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):               # COUNT[0]~COUNT[4]까지 누적 개수
    COUNTS[i] += COUNTS[i - 1]

# 3단계 : DATA의 맨 뒤부터 TEMP에 정렬하기
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1            # 누적 개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(*TEMP)