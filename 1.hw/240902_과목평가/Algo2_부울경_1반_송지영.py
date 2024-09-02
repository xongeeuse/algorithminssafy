import sys
sys.stdin = open('input2.txt')

'''
#1 0001001
#2 0001001 0001100 0001101
#3 1001000 0011001 1011000 1011000 1011101
'''

'''
1. 문자열 아스키 코드로 변환
2. 아스키 코드 2진수로 변환
3. 중위순회 순서대로 2진수 출력
'''

# 문자열 => 아스키 코드로 변환 저장
def str_to_ascii(data):
    for d in data:
        data_ascii.append(ord(d))

# 아스키코드로 얻은 값을 이진수로 변환
def dec_to_bin(data_ascii):
    for item in data_ascii:
        tmp = bin(item)[2:]
        while len(tmp) < 7:
            tmp = '0' + tmp
        data_bin.append(tmp)

# 2진수 7자리 중위 순회 순서
# [0, 4, 2, 5, 1, 6, 3, 7]
def inorder(node):
    left = node * 2
    right = node * 2 + 1
    if left <= 7:
        inorder(left)
    tree_inorder.append(node)
    if right <= 7:
        inorder(right)

# 중위 순회 순서대로 암호 출력하기
def solution(data):
    for d in data:
        result = []
        for i in range(1, 8):
            result.append(d[tree_inorder[i] - 1])
        print(''.join(result), end= ' ')
    print()



T = int(input())
for tc in range(1, T + 1):
    N = int(input())            # N 문자열의 길이
    data = input()
    # print(data)

    tree = list(range(N + 1))
    tree_inorder = [0]
    inorder(node=1)
    # print(tree_inorder)

    data_ascii = []             # 문자열 => 아스키 코드로 변환 저장할 리스트
    data_bin = []               # 아스키 코드 => 2진수로 변환 저장할 리스트'
    str_to_ascii(data)
    # print(data_ascii)
    dec_to_bin(data_ascii)
    # print(data_bin)

    print(f'#{tc}', end=' ')
    solution(data_bin)

