# list(f'{ord(data[i])}:08b')

print(f"{ord('1'):08b}")

result = []
data = '0123456789'
for d in data:
    result.append(f"{ord(d):08b}")

print(result)