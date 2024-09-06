import sys
sys.stdin = open('input.txt')

'''
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며!!!!!
visited 필요 없음
'''

def make_nums(i, j, current_num):
    if len(current_num) == 7:
        nums.add(current_num)
        return

    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        make_nums(ni, nj, current_num + data[ni][nj])

T = int(input())
for tc in range(1, T + 1):
    N = 4
    data = [input().split() for _ in range(N)]
    nums = set()
    for i in range(N):
        for j in range(N):
            make_nums(i, j, current_num=data[i][j])

    print(f'#{tc}', len(nums))
