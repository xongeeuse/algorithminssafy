s = 'abcde'
if s == s[::-1]:
    print('회문')
else:
    print('아님')



for i in range(N):
    for j in range(N):
        for k in range(M//2):
            A[i][j+k] == A[i][j+M-1-k]
