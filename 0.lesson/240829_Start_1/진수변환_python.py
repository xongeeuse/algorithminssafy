# 2진수 => 16진수 딕셔너리
bin_to_hex = {}

for i in range(16):
    bin_to_hex[f'{i:04b}'] = f'{i:X}'
print(bin_to_hex)

# 16진수 => 2진수 딕셔너리컴프리헨션으로 만들기
hex_to_bin = {f'{i:X}' : f'{i:04b}' for i in range(16)}
print(hex_to_bin)

