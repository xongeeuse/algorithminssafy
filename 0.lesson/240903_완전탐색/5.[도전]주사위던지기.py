N = 3
path = []

# my SOL
# '''
# 주사위 던지기
# 중복 가능하니까 위 경우와 조금 다름
# '''
# dice = list(range(1, 7))
# N = 3
#
# def run(lev):
#     if lev == N:
#         print(*path)
#         return
#
#     for i in range(6):
#         path.append(dice[i])
#         run(lev + 1)
#         path.pop()
# run(0)

def run(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i)
        path.pop()


run(0, 1)
