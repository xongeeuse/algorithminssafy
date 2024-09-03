data = ['A', 'B', 'C', 'D', 'E']
N = len(data)


def get_sub(target):
    global cnt

    for i in range(N):
        if target & 0x1:
            subset.append(data[i])
        target >>= 1
    if len(subset) >= 2:
        cnt += 1


cnt = 0
for target in range(1 << N):
    subset = []
    get_sub(target)


print(cnt)