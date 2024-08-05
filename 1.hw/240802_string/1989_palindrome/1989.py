import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    result = 0

    if word == word[::-1]:
        result = 1

    print(f'#{tc} {result}')



# another SOL
# for t in range(1, int(input())+1):
#     word = input()
#     print(f'#{t}', int(word == word[::-1]))



# another SOL 2
# def palindrome(s):
#     s = list(s)
#     N = len(s)
#     for i in range(N // 2):
#         if word[i] != word[N - 1 - i]:
#             return 0
#     return 1
#
# for tc in range(1, T+1):
#     word = input()
#
#     print(f'#{tc}', palindrome(word))



# another SOL 3
# for tc in range(1, T+1):
#     s = input()
#     N = len(s)
#     ans = 1
#     for i in range(N//2):
#         if s[i] != s[N-1-i]:
#             ans = 0
#             break
#
#     print(f'#{tc}', ans)
