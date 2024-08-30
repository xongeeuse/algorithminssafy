'''
16진수 문자로 이루어진 1차 배열에서 7bit씩 수를 묶어 10진수로 변환 출력하기

0F97A3
01D06079861D79F99F
'''

# 16진수 => 2진수
def hex_to_bin(num):
    global num_bin
    for n in num:
        num_bin += X_to_B[n]

# 2진수 => 10진수
def bin_to_dec(num):
    return int(num, base=2)


num = input()

X_to_B = {f'{i:X}': f'{i:04b}' for i in range(16)}     # 16진수 : 2진수 딕셔너리
num_bin = ''
hex_to_bin(num)
N = len(num_bin)


for i in range(0, N, 7):
    print(bin_to_dec(num_bin[i:i+7]), end=' ')