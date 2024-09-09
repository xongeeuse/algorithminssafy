# 16진수 => 10진수 변환
# 16진수 => 2진수 => 10진수

# hex_to_bin = {i for i in range(16) : }
hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
print(hex_to_bin)

passwords = {'B3B', '1F7', '81F', 'F75', '5E1', 'E1B', '1B3', '3B8', '75E', 'B81', '3B3'}
print(passwords)
passwords = list(passwords)
print(passwords)
passwords = sorted(passwords, reverse=True)
print(passwords)
# for password in passwords:
#     for p in password:
#

