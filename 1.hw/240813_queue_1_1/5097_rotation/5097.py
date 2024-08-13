import sys
sys.stdin = open('input.txt')

def rotate_num(data):
    cQ_N = N + 1                            # 원형 큐의 크기 : N + 1
    cQ = [0] * cQ_N
    rear = front = cnt = 0

    for d in data:                          # 데이터 원형 큐에 넣어주기
        cQ[rear] = d
        rear += 1

    while cnt < M:

        cQ[rear] = cQ[front]                # front값 rear로 넘겨주고
        cQ[front] = 0                       # front값은 0으로 리셋
        front = (front + 1) % cQ_N
        rear = (rear + 1) % cQ_N
        cnt += 1

    return cQ[front]



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # ######### short ver.
    # for i in range(M):
    #     data.append(data.pop(0))
    # print(f'#{tc}', data[0])

    print(f'#{tc}', rotate_num(data))