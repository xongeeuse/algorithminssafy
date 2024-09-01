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
    stack = []
    previous = data[0]
    for i in range(1, len(data)):
        if data[i] == previous:
            continue

    print(f'#{tc}', result)