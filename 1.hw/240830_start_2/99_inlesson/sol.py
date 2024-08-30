'''
0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어 10진수로 출력하기

input
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111

'''
def bin_to_dec(num):
    return int(num, base=2)


num = input()
N = len(num)
for i in range(0, N, 7):
    print(bin_to_dec(num[i:i+7]))