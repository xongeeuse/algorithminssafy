N = 5   # 데이터가 0~4까지의 정수인 경우 N = 4+1
data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * N
print(counts)

# 원소 개수 카운트
for x in data:
    counts[x] += 1

print(counts)

# 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수 반영
for i in range(1, N):
    counts[i] += counts[i - 1]

print(counts)

# 3단계
Temp = [0] * counts[N-1]

## 이해 못함
for j in range(len(Temp)-1, -1, -1):
    counts[data[j]] -= 1
    Temp[counts[data[j]]] = data[j]

print(Temp)