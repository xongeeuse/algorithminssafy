# 0~9 임의의 카드 6장 뽑았을 때
# 3장의 카드가 연속적인 번호를 갖는 경우 run
# 3장의 카드가 동일한 번호를 갖는 경우 triplet
# 6장의 카드가 run과 triplet으로만 구성된 경우 baby-gin

# 6자리 숫자 입력 받아 baby-gin 여부 찾기

# N = list(map(int, list(str(input()))))
N = list(map(int, input()))
print(N)

num = 456789
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10

print(c)