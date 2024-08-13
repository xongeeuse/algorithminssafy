from collections import deque

# 1 - 훨 씬 빠 름
deque_q = deque()
for i in range(1000000):
    deque_q.append(i)
for _ in range(1000000):
    deque_q.popleft()
print('end')



# 2 - 훨 씬 느 림
list_q = []

for i in range(1000000):
    list_q.append(i)
for _ in range(1000):
    list_q.pop(0)
print('end')
