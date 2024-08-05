s1 = 'abc'
s2 = 'abc'
print(s1 == s2)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)     # True

s3 = s1[:2] + 'c'
print(s3)
print(s2 == s3)     # True
print(s2 is s3)     # False
print(s1 is s2)     # True

# == 내용이 같은지
# is 주소값이 같은지


def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i

s= '123'
a = atoi(s)
print(a + 1)

s1 = "A"
print(ord('A'))
print(ord(s1))

print(chr(65))