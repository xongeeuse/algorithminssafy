import sys
sys.stdin = open('input.txt')

# 16진수 => 2진수 딕셔너리컴프리헨션으로 만들기
hex_to_bin = {f'{i:X}' : f'{i:04b}' for i in range(16)}
print(hex_to_bin)

T = int(input())
for tc in range(1, T + 1):
    N, data = input().split()
    N = int(N)
    print(f'#{tc}', end=' ')
    for d in data:
        print(hex_to_bin[d], end='')
    print()