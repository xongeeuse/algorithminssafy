Q_SIZE = 4
cQ = [0] * Q_SIZE
front = rear = 0

rear = (rear + 1) % Q_SIZE          # enqueue(1)
cQ[rear] = 1

rear = (rear + 1) % Q_SIZE          # enqueue(2)
cQ[rear] = 2

rear = (rear + 1) % Q_SIZE          # enqueue(3)
cQ[rear] = 3

rear = (rear + 1) % Q_SIZE          # enqueue(10)
cQ[rear] = 10

rear = (rear + 1) % Q_SIZE          # enqueue(20)
cQ[rear] = 20

rear = (rear + 1) % Q_SIZE          # enqueue(30)
cQ[rear] = 30

print(cQ)