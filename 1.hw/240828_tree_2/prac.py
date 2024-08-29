import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]

# 리스트를 최소 힙으로 변환
print('변환 전: ', numbers)
heapq.heapify(numbers)
print('heapify로 최소 힙 변환: ', numbers)

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 7)
heapq.heappush(heap, 4)
print('heappush 이용해 새로운 요소 추가: ', heap)

# 힙에서 가장 작은 요소 제거하고 반환
smallest = heapq.heappop(heap)
print(smallest)
print(heap)

# heapq 최대힙으로 구현하기
# 음수로 변환해서 최대 힙으로 구현
max_heap = []
for number in numbers:
    heapq.heappush(max_heap, -number)
print(max_heap)                         # [-10, -8, -7, -1, -4, -3, -5]

# 힙에서 가장 큰 요소 제거하고 반환
largest = -heapq.heappop(max_heap)      # 10
print(largest)