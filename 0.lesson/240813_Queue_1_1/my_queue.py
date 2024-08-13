# queue.py 라는 이름은 모듈과 겹쳐서 사용하지 않을 것!

N = 10
q = [0] * 10
front = -1
rear = -1

rear += 1           # enqueue(1)
q[rear] = 1
rear += 1           # enqueue(2)
q[rear] = 2
rear += 1           # enqueue(3)
q[rear] = 3

front += 1          # dequeue()
print(q[front])
front += 1          # dequeue()
print(q[front])
front += 1          # dequeue()
print(q[front])

# 자료 이해를 위해 간단한 큐를 구현하고 싶다면 사용 가능하지만
# append, pop은 자료가 복잡해지면 시간이 오래 걸림
# 언어와 무관하게 위 방식이 더 빠름
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))