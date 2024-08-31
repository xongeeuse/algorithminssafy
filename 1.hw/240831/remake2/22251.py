import sys
sys.stdin = open('input.txt')
'''
XAAYBBBCDDCZD
AABBBCCCDDD
XYZ
AAABBBCC
'''
def score():
    global result
    pass

T = int(input())
for tc in range(1, T + 1):
    data = input()
    result = 0


    print(f'#{tc}', result)