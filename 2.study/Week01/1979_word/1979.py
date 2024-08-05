import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    temp = []

    for i in range(N):
        cnt_r = 0
        cnt_c = 0
        max_cnt_r = 0
        max_cnt_c = 0
        for j in range(N):
            if data[i][j] == 1:
                cnt_r += 1
                if max_cnt_r < cnt_r:
                    max_cnt_r = cnt_r
            else: cnt_r = 0

            if data[j][i] == 1:
                cnt_c += 1
                if max_cnt_c < cnt_c:
                    max_cnt_c = cnt_c
            else: cnt_c = 0

        temp.append(max_cnt_r)
        temp.append(max_cnt_c)

    result = 0
    for t in temp:
        if t == K:
            result += 1

    print(f'#{tc}', result)


    ##################################틀림
    # for tc in range(1, T + 1):
    #     N, K = map(int, input().split())
    #     data = [list(map(int, input().split())) for _ in range(N)]
    #     result = 0
    #
    #     for i in range(N):
    #         cnt_r = 0
    #         cnt_c = 0
    #         max_cnt_r = 0
    #         max_cnt_c = 0
    #         for j in range(N):
    #             if data[i][j] == 1:
    #                 cnt_r += 1
    #                 if max_cnt_r < cnt_r:
    #                     max_cnt_r = cnt_r
    #             else:
    #                 cnt_r = 0
    #
    #             if data[j][i] == 1:
    #                 cnt_c += 1
    #                 if max_cnt_c < cnt_c:
    #                     max_cnt_c = cnt_c
    #             else:
    #                 cnt_c = 0
    #
    #         if max_cnt_c == K:
    #             result += 1
    #         if max_cnt_r == K:
    #             result += 1
    #
    #     print(result)