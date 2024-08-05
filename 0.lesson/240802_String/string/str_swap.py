# 문자열 뒤집기 swap 이용
s1 = list(input())      # 'algorithm'
N = len(s1)

for i in range(N//2):
    s1[i], s1[N-1-i] = s1[N-1-i], s1[i]

print(''.join(s1))


# 슬라이싱 이용한 경우
s2 = 'hello'
print(s2[::-1])














