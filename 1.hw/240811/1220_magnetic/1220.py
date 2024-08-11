import sys
sys.stdin = open('input.txt')

'''
#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490
'''

T = 10
for tc in range(1, T+1):
    N = int(input())                        # 테이블 크기 N x N
    data = [list(map(int, input().split())) for _ in range(N)]
